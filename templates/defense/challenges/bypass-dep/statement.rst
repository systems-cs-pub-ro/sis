Disassemble the `vuln` executable, see where the buffer overflow happens and what is the offset from the buffer start to the return address. The system is using DEP (*Data Execution Prevention*) and you cannot inject a shellcode. However we assume the executable runs on a non-ASLR environment. In order to create that, run the command below to create a non-ASLR shell:

   ::

       setarch $(uname -m) -R /bin/bash

   Now you can create a shell by following the below steps:

   a. Use the skeleton in the `exploit.py` script.

   b. Use GDB to determine the address of the `system()` function.

   c. Use GDB to determine the address of the `"/bin/sh"` (or just the `"sh"`) string.

   d. Use the above information to craft a payload in `exploit.py` that manages to overwrite the return address of the `reader()` function and call `system("/bin/sh")` or `system("sh")`.

   This is a *return-to-libc* attack.

