.fmt:
	.asciz "%d\n"
.text


.globl _start

_start:

	push $5

	push $9

	pop %rdx
	pop %rcx
	add %rdx, %rcx
	push %rcx

	pop %rdx
	mov %rdx, %rsi
	push %rdx
	xor %rax, %rax
	mov $.fmt, %rdi
	call printf

	push $3

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

