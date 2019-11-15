BITS 32

    jmp string          ; Use call trampoline trick.
back:
    pop ecx             ; Pop string address from stack.
    mov edx, 14         ; Message length is 14 bytes.
    mov ebx, 1          ; Print to standard output (fd = 1).
    mov eax, 4          ; __NR_write
    int 0x80
    xor ebx, ebx        ; exit value = 0
    mov eax, 1          ; __NR_exit
    int 0x80
string:
    call back
    db "Hello, World!", 10, 0
