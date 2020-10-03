Disassemble the `vuln` executable, see where the buffer overflow happens and what is the offset from the buffer start to the return address. The system is using DEP (*Data Execution Prevention*) and you cannot inject a shellcode. We assume the executable runs on an ASLR-enabled environment so you cannot easily determine the address of the `system()` function call and the `"/bin/sh"` string. You can however use the address of `system()` in PLT and use the `"sh"` string that is, fortunatelly, part of the executable.

   Now you can create a shell by following the below steps:

   a. Use the skeleton in the `exploit.py` script.

   b. Use GDB to determine the address of the `system()` function PLT entry.

   c. Use GDB to determine the address of the `"sh"` string in the executable.

   d. Use the above information to craft a payload in `exploit.py` that manages to overwrite the return address of the `reader()` function and call `system@plt("sh")`.

   This is a *return-to-plt* attack, a particular form of the *return-to-libc* attack.
