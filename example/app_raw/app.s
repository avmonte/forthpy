.fmt:
	.asciz "%d\n"
.text


.globl _start

_start:

	push $7

	push $9

	pop %rdx
	mov %rdx, %rsi
	push %rdx
	xor %rax, %rax
	mov $.fmt, %rdi
	call printf

	pop %rdx

	push $5

	pop %rdx
	pop %rcx
	imul %rdx, %rcx
	push %rcx

	pop %rdx
	mov %rdx, %rsi
	push %rdx
	xor %rax, %rax
	mov $.fmt, %rdi
	call printf

	mov $60, %rax
	pop %rdi
	syscall

