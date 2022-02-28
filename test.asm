section .text
global _start

_start: jmp _0

_0: jmp _1

section .bss
v_foo: resb 9

section .data
_somedata: db 255

section .text
_1:
    mov eax, 1
    mov ebx, 0
    int 0x80
