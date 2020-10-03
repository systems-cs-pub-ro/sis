Use ``checksec.sh`` to audit the security of the executables on your system. You can download ``checksec.sh`` from the `following link`_.

.. _following link: https://raw.githubusercontent.com/slimm609/checksec.sh/master/checksec

Or you can use pwntools_ as a wrapper of ``checksec``.

.. _pwntools: http://docs.pwntools.com/en/stable/commandline.html#pwn-checksec

Use GCC and its options to create executables with all sorts of combinations (NX, PIE, stack canary, RELRO). Build (compile and link) an executable with all hardening options on::

  $ checksec a.out
    [...]
    Arch:     amd64-64-little
    RELRO:    Full RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      PIE enabled

And build (compile and link) an executable with all hardening options off::

  $ checksec a.out
    [...]
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX disabled
    PIE:      No PIE (0x400000)
    RWX:      Has RWX segments
