.data

file:		.asciiz "input"
contents:	.space 11000

.text

.globl main
main:
	jal read_file
	jal solve
	j program_end
	
	
solve:
	la $a3 contents
	add $s1 $0 $0 # highest calorie total elf
	add $s2 $0 $0 # second highest calorie total elf
	add $s3 $0 $0 # third highest calorie total elf
same_elf:
	add $s0 $0 $0 # current elf calorie total
	
same_elf_loop:
	beq $s4 1 file_end
	move $a0 $a3
	move $s6 $ra
	jal read_int
	move $ra $s6
	move $a3 $a0
	add $s0 $s0 $v0
	addi $a3 $a3 2
	lb $t0 0($a3)
	seq $s4 $t0 0
	beq $t0 0 new_elf
	beq $t0 10 new_elf
	j same_elf_loop
	
new_elf:
	addi $a3 $a3 1
	bgt $s0 $s1 new_first
	bgt $s0 $s2 new_second
	bgt $s0 $s3 new_third
	j same_elf
	
new_first:
	move $s3 $s2
	move $s2 $s1
	move $s1 $s0
	j same_elf
new_second:
	move $s3 $s2
	move $s2 $s0
	j same_elf
new_third:
	move $s3 $s0
	j same_elf
	
file_end:
	move $a0 $s1
	li $v0 1
	syscall
	li $a0 10
	li $v0 11
	syscall
	add $a0 $s1 $s2
	add $a0 $a0 $s3
	li $v0 1
	syscall
	jr $ra
	

read_int:
	# pass $a0 = memory location to start reading from
	# returns $a0 memory location stopped reading
	# $v0 int
	li $t0 1 # tens, hundreds etc.
	add $v0 $0 $0 # output
	li $t2 10
	addi $t3 $a0 1
read_int_get_length:
	lb $t1 0($t3)
	ble $t1 47 read_int_loop
	bge $t1 58 read_int_loop
	mult $t0 $t2
	mflo $t0
	# is digit
	addi $t3 $t3 1
	j read_int_get_length

read_int_loop:
	lb $t1 0($a0)
	addi $t1 $t1 -48
	mult $t1 $t0
	mflo $t4
	add $v0 $v0 $t4
	beq $t0 1 read_int_end
	div $t0 $t2
	mflo $t0
	addi $a0 $a0 1
	j read_int_loop
	
read_int_end:
	jr $ra

read_file:
	li $v0 13 		# open file
	la $a0 file
	add $a1 $0 $0
	add $a2 $0 $0
	syscall
	add $s0 $v0 $0
	li $v0 14		# read file into "contents"
	add $a0 $s0 $0
	la $a1 contents
	li $a2 11000
	syscall
	jr $ra
	
	
        
program_end:
	li $v0 10
	syscall