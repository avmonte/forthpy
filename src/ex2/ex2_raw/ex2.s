.fmt:
	.asciz "%d\n"
.text


.globl _start

_start:

	push $17

	push $5

	pop %rcx
	pop %rax
	cqo
	idiv %rcx
	push %rax

	pop %rdx
	mov %rdx, %rsi
	push %rdx
	xor %rax, %rax
	mov $.fmt, %rdi
	call printf

	push $2

	push $137

	pop %rdx

	pop %rcx
	pop %rax
	cqo
	idiv %rcx
	push %rdx

	pop %rdx
	mov %rdx, %rsi
	push %rdx
	xor %rax, %rax
	mov $.fmt, %rdi
	call printf

	mov $60, %rax
	pop %rdi
	syscall

