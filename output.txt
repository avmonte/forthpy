
.global _start

_start:
	push 8

	push 8

	pop %rsp, %rdx
	pop %rsp, %rcx
	add $rdx, %rcx
	push %rcx

	push %rsp

	pop %rsp, %rdx
	pop %rsp, %rcx
	push $rdx
	push %rcx

	ret

