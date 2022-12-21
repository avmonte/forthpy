.fmt:
	.asciz "%d\n"
.text


.globl _start

_start:

	push $3

	pop %rdx
	mov %rdx, %rsi
	push %rdx
	xor %rax, %rax
	mov $.fmt, %rdi
	call printf

	push $6

	pop %rdx
	mov %rdx, %rsi
	push %rdx
	xor %rax, %rax
	mov $.fmt, %rdi
	call printf

	pop %rdx
	push %rdx
	push %rdx

	pop %rdx
	mov %rdx, %rsi
	push %rdx
	xor %rax, %rax
	mov $.fmt, %rdi
	call printf

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

	pop %rdx
	pop %rcx
	push %rdx
	push %rcx

	pop %rdx
	mov %rdx, %rsi
	push %rdx
	xor %rax, %rax
	mov $.fmt, %rdi
	call printf

	pop %rdx
	pop %rcx
	sub %rdx, %rcx
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

