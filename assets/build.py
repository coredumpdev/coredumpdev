#!/usr/bin/env python3
"""Generate every SVG used by the profile README.

Run:  python3 assets/build.py

Animation rule: every animated attribute's *base* value equals its final
frame, so the artwork stays complete and legible if SMIL is unsupported or
stripped. Reveals are done with keyTimes inside a single begin="0s"
animation rather than a delayed begin, which would flash the base value
before the animation takes over.
"""

import os

W = 840
MONO = 'ui-monospace, &quot;SF Mono&quot;, SFMono-Regular, Menlo, Consolas, &quot;Liberation Mono&quot;, monospace'

BG, PANEL, BORDER, BORDER2 = "#0d1117", "#161b22", "#30363d", "#21262d"
MUTED, DIM, TEXT, SUBTLE = "#6e7681", "#5b6570", "#c9d1d9", "#8b949e"
GREEN, BLUE, PURPLE, ORANGE, CYAN, GOLD, RED = (
    "#3fb950", "#58a6ff", "#bc8cff", "#f0883e", "#39c5cf", "#d29922", "#ff7b72")

OUT = os.path.dirname(os.path.abspath(__file__))


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def appear(begin, dur, fade=0.18):
    """Opacity reveal at `begin` seconds within a `dur`-long timeline."""
    k = f"0;{begin / dur:.4f};{(begin + fade) / dur:.4f};1"
    return (f'<animate attributeName="opacity" values="0;0;1;1" '
            f'keyTimes="{k}" dur="{dur}s" begin="0s" fill="freeze"/>')


def wipe(begin, dur, width, fade=0.30):
    """Left-to-right width wipe at `begin` seconds within `dur`."""
    k = f"0;{begin / dur:.4f};{(begin + fade) / dur:.4f};1"
    return (f'<animate attributeName="width" values="0;0;{width};{width}" '
            f'keyTimes="{k}" dur="{dur}s" begin="0s" fill="freeze"/>')


def chrome(title, h):
    """Terminal window frame: rounded panel, title bar, traffic lights."""
    return f'''  <rect x="0.5" y="0.5" width="{W - 1}" height="{h - 1}" rx="10" fill="{BG}" stroke="{BORDER}"/>
  <path d="M0.5 10.5a10 10 0 0 1 10-10h{W - 21}a10 10 0 0 1 10 10V36H0.5z" fill="{PANEL}" stroke="{BORDER}"/>
  <circle cx="22" cy="18" r="5.5" fill="#ff5f56"/>
  <circle cx="41" cy="18" r="5.5" fill="#ffbd2e"/>
  <circle cx="60" cy="18" r="5.5" fill="#27c93f"/>
  <text class="m" x="{W // 2}" y="22" text-anchor="middle" fill="#7d8590" font-size="11.5">{esc(title)}</text>'''


def svg(h, body, defs="", label=""):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{h}" viewBox="0 0 {W} {h}" role="img" aria-label="{esc(label)}">
  <defs>
    <style>.m {{ font-family: {MONO}; font-size: 13px; }}</style>
{defs}  </defs>
{body}
</svg>
'''


def write(name, content):
    path = os.path.join(OUT, name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  {name}  ({len(content)} bytes)")


# ---------------------------------------------------------------- session

# The banner is a real hexdump: these bytes are what the ASCII column spells
# out. Each line below is exactly 16 bytes, one dump row. Keep it that way.
BANNER = (
    b"coredumpdev\x00\x00\x00\x00\x00"
    b"Muzaffer Tolga Y"
    b"akar\nSoftware En"
    b"gineer @ Zeta De"
    b"fence\nKadikoy, I"
    b"stanbul\x00\x00\x00\x00\x00\x00\x00\x00\x00"
)

PROSE = [
    "Software engineer at Zeta Defence. I gravitate to the layers",
    "below the framework: kernels, bare-metal MCUs, packet paths,",
    "and the parts of a program that only make sense in a debugger.",
    "Occasionally I surface into userland to make pixels move fast.",
]


def hexdump(blob, cols=16, group=2):
    """xxd -style rows of (offset, hex, ascii) — the banner's source of truth."""
    rows = []
    for off in range(0, len(blob), cols):
        chunk = blob[off:off + cols]
        hx = "".join(chunk[i:i + group].hex().ljust(group * 2) + " "
                     for i in range(0, cols, group))
        asc = "".join(chr(b) if 32 <= b < 127 else "." for b in chunk)
        rows.append((f"{off:08x}: ", hx, asc))
    return rows


def build_session():
    cmd1 = "xxd -l %d /var/crash/coredumpdev.core" % len(BANNER)
    cmd2 = "whoami --verbose"
    rows = hexdump(BANNER)

    # Layout flows from the content, so editing BANNER or PROSE just works.
    y_hex = 90
    y_cmd2 = y_hex + len(rows) * 20 + 10
    y_prose = y_cmd2 + 26
    y_prompt = y_prose + len(PROSE) * 20 + 12
    H = y_prompt + 24

    # Timeline: type, dump, type, speak. Each stage waits for the previous.
    t2 = 0.95 + 0.19 * len(rows) + 0.30
    t3 = t2 + 0.85
    D = round(t3 + 0.20 * len(PROSE) + 0.40, 2)

    defs = f'''    <clipPath id="t1"><rect x="0" y="50" height="20" width="360">
      <animate attributeName="width" values="18;360" dur="0.85s" begin="0s" fill="freeze"/></rect></clipPath>
    <clipPath id="t2"><rect x="0" y="{y_cmd2 - 14}" height="20" width="220">
      <animate attributeName="width" values="18;220" dur="0.7s" begin="{t2:.2f}s" fill="freeze"/></rect></clipPath>
'''

    b = [chrome("coredumpdev — zsh", H)]
    b.append(f'  <g clip-path="url(#t1)"><text class="m" x="24" y="64" xml:space="preserve">'
             f'<tspan fill="{GREEN}">$ </tspan><tspan fill="{TEXT}">{esc(cmd1)}</tspan></text></g>')

    for i, (off, hx, asc) in enumerate(rows):
        b.append(f'  <text class="m" x="24" y="{y_hex + i * 20}" xml:space="preserve">'
                 f'<tspan fill="{MUTED}">{off}</tspan><tspan fill="{DIM}">{hx}</tspan>'
                 f'<tspan fill="{GREEN}">{esc(asc)}</tspan>{appear(0.95 + 0.19 * i, D)}</text>')

    # Hidden until t2 so the typing clip never flashes its base width.
    b.append(f'  <g opacity="0">{appear(t2, D, 0.01)}'
             f'<g clip-path="url(#t2)"><text class="m" x="24" y="{y_cmd2}" xml:space="preserve">'
             f'<tspan fill="{GREEN}">$ </tspan><tspan fill="{TEXT}">{esc(cmd2)}</tspan></text></g></g>')

    for i, line in enumerate(PROSE):
        b.append(f'  <text class="m" x="24" y="{y_prose + i * 20}" fill="{SUBTLE}" xml:space="preserve">'
                 f'{esc(line)}{appear(t3 + 0.20 * i, D)}</text>')

    b.append(f'  <text class="m" x="24" y="{y_prompt}" fill="{GREEN}" xml:space="preserve">$ </text>')
    b.append(f'  <rect x="40" y="{y_prompt - 11}" width="8" height="14" fill="{GREEN}">'
             f'<animate attributeName="opacity" values="1;1;0;0;1" keyTimes="0;0.45;0.5;0.95;1" '
             f'dur="1.1s" repeatCount="indefinite"/></rect>')

    spoken = BANNER.replace(b"\x00", b"").decode().replace("\n", ", ")
    write("session.svg", svg(H, "\n".join(b), defs,
                             f"Terminal: a hexdump whose ASCII column reads {spoken}. "
                             f"Below it: {' '.join(PROSE)}"))


# ------------------------------------------------------------------ stack

REGIONS = [
    ("00400000-0040c000", "r-xp", "[ text ]", GREEN,  "C · C++ · Assembly · Rust"),
    ("0060a000-00612000", "rw-p", "[ data ]", BLUE,   "TypeScript · Python · Lua · Swift"),
    ("7f0a4000-7f0a5000", "r--p", "[rodata]", PURPLE, "Linux · STM32 · MSP430 · RTOS"),
    ("7ffd1000-7ffd2000", "rw-p", "[stack ]", ORANGE, "Qt · React · WebGL2 · Electron"),
    ("7fff0000-7fff1000", "r-xp", "[ vdso ]", CYAN,   "gdb · rizin · perf · Wireshark"),
]


def build_stack():
    D, H = 1.8, 272
    defs = "".join(
        f'    <clipPath id="r{i}"><rect x="0" y="{40 + i * 44}" height="38" width="{W}">'
        f'{wipe(0.10 + 0.18 * i, D, W)}</rect></clipPath>\n'
        for i in range(len(REGIONS)))

    b = [f'  <rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="10" fill="{BG}" stroke="{BORDER}"/>',
         f'  <text class="m" x="20" y="26" font-size="12" xml:space="preserve">'
         f'<tspan fill="{GREEN}">$ </tspan><tspan fill="#7d8590">cat /proc/self/maps</tspan></text>']

    for i, (addr, perm, seg, col, tech) in enumerate(REGIONS):
        y, ty = 42 + i * 44, 64 + i * 44
        b.append(f'''  <g clip-path="url(#r{i})">
    <rect x="16" y="{y}" width="808" height="34" rx="7" fill="{PANEL}"/>
    <rect x="16" y="{y}" width="3.5" height="34" fill="{col}"/>
    <text class="m" x="34"  y="{ty}" font-size="12" fill="{MUTED}">{addr}</text>
    <text class="m" x="176" y="{ty}" font-size="12" fill="{DIM}">{perm}</text>
    <text class="m" x="224" y="{ty}" font-size="12.5" fill="{col}">{esc(seg)}</text>
    <text class="m" x="320" y="{ty}" fill="{TEXT}">{esc(tech)}</text>
  </g>''')

    write("stack.svg", svg(H, "\n".join(b), defs,
                           "Tech stack drawn as a process memory map: text segment C, C++, Assembly, "
                           "Rust; data TypeScript, Python, Lua, Swift; rodata Linux, STM32, MSP430, "
                           "RTOS; stack Qt, React, WebGL2, Electron; vdso gdb, rizin, perf, Wireshark."))


# --------------------------------------------------------------- projects

PROJECTS = [
    ("photon", GREEN, "TypeScript", "WebGL2 scientific plotting — 1e6 points at 60 fps"),
    ("disasm-ai", BLUE, "TypeScript", "AI-assisted reverse engineering, built on rizin"),
    ("in-mem-db", ORANGE, "C", "An in-memory database written from scratch"),
    ("basic-os", PURPLE, "C++", "An x86 kernel, from the bootloader up"),
    ("stm32-bare-matel-f429zi", CYAN, "Assembly", "Bare-metal Cortex-M4 — no HAL, no RTOS"),
    ("pcap-capture", GOLD, "C++", "Packet capture and dissection"),
]


def build_projects():
    H, D = 46, 1.2
    for i, (name, col, lang, desc) in enumerate(PROJECTS):
        defs = (f'    <clipPath id="w"><rect x="0" y="0" height="{H}" width="{W}">'
                f'{wipe(0.06 * i, D, W)}</rect></clipPath>\n')
        b = f'''  <g clip-path="url(#w)">
    <rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="8" fill="{PANEL}" stroke="{BORDER2}"/>
    <rect x="1" y="1" width="3.5" height="{H - 2}" fill="{col}"/>
    <text class="m" x="24"  y="29" font-weight="600" fill="{BLUE}">{esc(name)}</text>
    <text class="m" x="252" y="29" font-size="12.5" fill="{SUBTLE}">{esc(desc)}</text>
    <text class="m" x="{W - 24}" y="29" font-size="11.5" fill="{col}" text-anchor="end">{esc(lang)}</text>
  </g>'''
        write(f"proj-{name}.svg", svg(H, b, defs, f"{name} — {desc} ({lang})"))


# ------------------------------------------------------------------- misc

DMESG = [
    ("2451.881204", "photon", "1e6 points through WebGL2, holding 60fps"),
    ("2453.019877", "disasm-ai", "rizin + rz-ghidra under an Electron shell"),
    ("2455.442310", "kernel", "reading the Linux tree, one subsystem at a time"),
    ("2457.113095", "tolga", "always up for a talk about cache lines and MMUs"),
]


def build_now():
    D, H = 2.0, 214
    b = [chrome("coredumpdev — dmesg", H),
         f'  <text class="m" x="24" y="64" xml:space="preserve">'
         f'<tspan fill="{GREEN}">$ </tspan><tspan fill="{TEXT}">dmesg | tail -4</tspan></text>']

    for i, (ts, unit, msg) in enumerate(DMESG):
        b.append(f'  <text class="m" x="24" y="{92 + i * 22}" font-size="12.5" xml:space="preserve">'
                 f'<tspan fill="{MUTED}">[ {ts}] </tspan><tspan fill="{CYAN}">{unit}: </tspan>'
                 f'<tspan fill="{SUBTLE}">{esc(msg)}</tspan>{appear(0.2 + 0.22 * i, D)}</text>')

    b.append(f'  <text class="m" x="24" y="190" xml:space="preserve">'
             f'<tspan fill="{GREEN}">$ </tspan><tspan fill="{TEXT}">./coredumpdev</tspan>'
             f'<tspan fill="{RED}">   Segmentation fault (core dumped)</tspan>{appear(1.3, D)}</text>')

    write("now.svg", svg(H, "\n".join(b), "",
                         "Terminal: kernel-log styled lines about current work, ending with "
                         "./coredumpdev — Segmentation fault (core dumped)."))


def build_contact():
    H, D = 46, 1.0
    defs = (f'    <clipPath id="w"><rect x="0" y="0" height="{H}" width="{W}">'
            f'{wipe(0.05, D, W)}</rect></clipPath>\n')
    b = f'''  <g clip-path="url(#w)">
    <rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="8" fill="{PANEL}" stroke="{BORDER2}"/>
    <rect x="1" y="1" width="3.5" height="{H - 2}" fill="{GREEN}"/>
    <text class="m" x="24" y="29" xml:space="preserve"><tspan fill="{GREEN}">$ </tspan><tspan fill="{DIM}">mail -s "hi" </tspan><tspan fill="{BLUE}">muzaffertolgayakar@gmail.com</tspan></text>
    <text class="m" x="{W - 24}" y="29" font-size="11.5" fill="{MUTED}" text-anchor="end">Kadıköy, İstanbul</text>
  </g>'''
    write("contact.svg", svg(H, b, defs, "Email muzaffertolgayakar@gmail.com — Kadikoy, Istanbul"))


if __name__ == "__main__":
    print("building SVGs:")
    build_session()
    build_stack()
    build_projects()
    build_now()
    build_contact()
    print("done")
