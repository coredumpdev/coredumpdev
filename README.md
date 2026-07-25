```console
$ xxd -l 112 /var/crash/coredumpdev.core
00000000: 636f 7265 6475 6d70 6465 7600 0000 0000  coredumpdev.....
00000010: 4d75 7a61 6666 6572 2054 6f6c 6761 2059  Muzaffer Tolga Y
00000020: 616b 6172 0a5a 6574 6120 4465 6665 6e63  akar.Zeta Defenc
00000030: 6520 2f20 4b61 6469 6b6f 792c 2049 5354  e / Kadikoy, IST
00000040: 0a73 7973 7465 6d73 202e 2065 6d62 6564  .systems . embed
00000050: 6465 6420 2e20 7265 7665 7273 652d 656e  ded . reverse-en
00000060: 6769 6e65 6572 696e 6700 0000 0000 0000  gineering.......
```

```console
$ whoami --verbose

Systems and embedded engineer at Zeta Defence. I spend most of my time
a few layers below the framework: kernels, bare-metal MCUs, packet
paths, and the parts of a program that only make sense in a debugger.

Occasionally I surface into userland to make pixels move fast.
```

<br>

### `$ cat /proc/self/maps`

```console
00400000-0040c000 r-xp  [ text ]    C · C++ · Assembly · Rust
0060a000-00612000 rw-p  [ data ]    TypeScript · Python · Lua · Swift
7f0a4000-7f0a5000 r--p  [rodata]    Linux · STM32 · MSP430 · RTOS
7ffd1000-7ffd2000 rw-p  [stack ]    Qt · React · WebGL2 · Electron
7fff0000-7fff1000 r-xp  [ vdso ]    gdb · rizin · perf · Wireshark
```

<br>

### `$ ls -lt ~/src`

<pre>
drwxr-xr-x  <a href="https://github.com/coredumpdev/photon">photon/</a>                   WebGL2 plotting, 1e6 pts @ 60fps
drwxr-xr-x  <a href="https://github.com/coredumpdev/disasm-ai">disasm-ai/</a>                multi-arch RE tool on rizin
drwxr-xr-x  <a href="https://github.com/coredumpdev/in-mem-db">in-mem-db/</a>                in-memory database in C
drwxr-xr-x  <a href="https://github.com/coredumpdev/basic-os">basic-os/</a>                 x86 kernel from scratch
drwxr-xr-x  <a href="https://github.com/coredumpdev/stm32-bare-matel-f429zi">stm32-bare-matel-f429zi/</a>  bare-metal Cortex-M4, pure asm
drwxr-xr-x  <a href="https://github.com/coredumpdev/pcap-capture">pcap-capture/</a>             packet capture &amp; dissection
</pre>

<br>

### `$ dmesg | tail -4`

```console
[ 2451.881204] photon: 1e6 points through WebGL2, holding 60fps
[ 2453.019877] disasm-ai: rizin + rz-ghidra under an Electron shell
[ 2455.442310] kernel: reading the Linux tree, one subsystem at a time
[ 2457.113095] tolga: always up for a talk about cache lines and MMUs
```

<br>

### `$ ss -tlnp`

<pre>
Proto  Local Address:Port    State    Process
tcp    github.com:443        LISTEN   <a href="https://github.com/coredumpdev">github.com/coredumpdev</a>
tcp    smtp:25               LISTEN   <a href="mailto:muzaffertolgayakar@gmail.com">muzaffertolgayakar@gmail.com</a>
</pre>

<br>

### `$ cat /sys/class/github/coredumpdev/stats`

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats.vercel.app/api?username=coredumpdev&show_icons=true&hide_border=true&include_all_commits=true&bg_color=00000000&title_color=3fb950&text_color=8b949e&icon_color=3fb950">
  <img height="150" src="https://github-readme-stats.vercel.app/api?username=coredumpdev&show_icons=true&hide_border=true&include_all_commits=true&bg_color=00000000&title_color=1a7f37&text_color=57606a&icon_color=1a7f37" alt="GitHub stats">
</picture>
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats.vercel.app/api/top-langs/?username=coredumpdev&layout=compact&hide_border=true&langs_count=8&bg_color=00000000&title_color=3fb950&text_color=8b949e">
  <img height="150" src="https://github-readme-stats.vercel.app/api/top-langs/?username=coredumpdev&layout=compact&hide_border=true&langs_count=8&bg_color=00000000&title_color=1a7f37&text_color=57606a" alt="Top languages">
</picture>

<br>

<details>
<summary><code>$ LANG=tr_TR.UTF-8 ./whoami</code></summary>

<br>

```console
$ ./whoami --ayrintili

Zeta Defence'te sistem ve gömülü yazılım mühendisiyim. Vaktimin çoğu
framework'lerin birkaç kat altında geçiyor: çekirdekler, bare-metal
mikrodenetleyiciler, paket yolları ve bir programın yalnızca debugger
içinde anlam kazanan kısımları.

Arada userland'e çıkıp piksellerin hızlı akmasını sağlıyorum.
```

**Öne çıkan işler**

- [photon](https://github.com/coredumpdev/photon) — WebGL2 tabanlı bilimsel çizim kütüphanesi. React/Vue/Svelte bağlayıcılarıyla, milyonlarca noktayı 60fps'te çiziyor.
- [disasm-ai](https://github.com/coredumpdev/disasm-ai) — AI destekli, çok mimarili tersine mühendislik aracı (Electron + rizin + rz-ghidra).
- [in-mem-db](https://github.com/coredumpdev/in-mem-db) — C ile yazılmış in-memory veritabanı.
- [basic-os](https://github.com/coredumpdev/basic-os) — Sıfırdan x86 çekirdeği.
- [stm32-bare-matel-f429zi](https://github.com/coredumpdev/stm32-bare-matel-f429zi) — Saf Assembly ile bare-metal Cortex-M4.

**İletişim** — [muzaffertolgayakar@gmail.com](mailto:muzaffertolgayakar@gmail.com) · Kadıköy, İstanbul

</details>

<br>

```console
$ ./coredumpdev
Segmentation fault (core dumped)
```
