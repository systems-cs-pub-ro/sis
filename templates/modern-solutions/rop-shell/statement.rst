Open the session task archive and access the ``rop-shell/`` subfolder. Your
goal is to open a shell by calling ``system("/bin/sh")``. You can jump
directly to where ``system()`` is called. You need to store the address of
``sh`` in RDI using a gadget. You can find the address of ``sh`` in the
executable by using ``find`` in GDB PEDA.

Construct the ROP-based payload in ``exploit.py`` similar to the
``exploit.py`` file in the ``rop-demo/`` subfolder.

You can look for ROP gadgets by issuing the command

        $ ROPgadget --binary vuln
