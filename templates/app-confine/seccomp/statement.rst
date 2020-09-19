Now we want to use sandboxing (``seccomp``) to allow the program to open the ``../jail/a.txt`` file, but not the ``../b.txt`` file.

Access the ``seccomp/`` subfolder. Inspect the ``exec.c`` file and see what it does and what calls should succeed or not. Compile it using ``make``. Run ``strace ./exec`` and see what calls are allowed and what calls are not allowed.

Update the ``exec.c`` file to enforce and check that read and write is allowed to the ``a.txt`` file, but only read is allowed to the ``b.txt`` file.

You need the ``libseccomp-dev:i386`` installed on the system. To install it run::

  sudo apt install gcc-multilib libseccomp-dev:i386

**Bonus**: Update the ``exec.c`` program to invoke the ``read`` and ``write`` system calls from inside a shellcode, similar to way its done in the ``shellcode/run-shellcode/exec.c``.
