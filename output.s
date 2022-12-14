
.global _start

_start:
	push $8

	push $8

	pop %rdx
	pop %rcx

	add $rdx, %rcx

	push %rcx

	pop %rdx
	push %rdx
	push %rdx

	pop %rdx
	pop %rcx
	push $rdx
	push %rcx

	ret

