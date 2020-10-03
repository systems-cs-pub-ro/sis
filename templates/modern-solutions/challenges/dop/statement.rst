First make sure you have a recent version of Clang/LLVM (3.8+) installed. If
you use the lab machines, use ``apt-get`` to install the ``clang-4.0`` package.

Open the session task archive and access the ``dop/`` subfolder.
Open ``dop.c``. What is the vulnerability? Notice there is a buffer overflow in
``f`` and that ``f`` contains a while loop that acts as an interpreter.

Open ``payload.c`` and study the example payload. What does it do? Fill in the
missing addresses in ``payload.c``. Generate the payload and feed it to
``dop``. It should print ``“End of program: FAILAA!”``.

Devise a similar payload that makes dop print ``“End of program: SISPWN!”``.

Recompile dop with the ``-fsanitize=safe-stack`` flag and run the exploit again.
What happened? Why?
