Access the ``shellcode/`` subfolder. We assume a shellcode is injected maliciously inside an executable and we want to use different mechanisms to protect it. To simplify things we add the shellcode in the source code and compile it to execute the shellcode.

There are two subfolders: ``generate-shellcode/`` for generating a shellcode and ``run-shellcode/`` for running a shellcode inside an executable. Use ``make print`` in ``generate-shellcode/`` to generate the shellcode. It is part of the ``shellcode`` array in ``exec.c`` in ``run-shellcode/``.

Test what it does by running ``strace ./exec`` in ``generate-shellcode``.

Inspect the shellcode implementation in ``shellcode.asm``. Update the shellcode to **also** open the two files from ``../../jail/a.txt`` and ``../../b.txt`` using the ``open`` system call: the first argument (in ``ebx``) is a pointer to the string denoting the filename, the second argument (in ``ecx``) is ``O_RDONLY`` (see its numeric value in ``/usr/include/bits/fcntl-linux.h``).

Generate the new shellcode (using ``make print``), replace it in ``exec.c``, recompile the ``exec`` executable, and then test it again by running ``strace ./vuln``.
