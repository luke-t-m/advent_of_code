.data

file:		.asciiz "input"
contents:	.space 600

.text

.globl main
main:

	jal read_file
	jal solve
solved:
	li $v0 1
	move $a0 $t6
	syscall
	li $v0 11
	li $a0 32
	syscall
	li $v0 1
	move $a0 $t7
	syscall
	abs $t6 $t6
	abs $t7 $t7
	add $t6 $t6 $t7
	li $v0 11
	li $a0 10
	syscall
	li $v0 1
	move $a0 $t6
	syscall
	j program_end
	
solve:
	la $s0 contents # address
	add $s1 $0 $0 # direction
	add $t6 $0 $0 # x
	add $t7 $0 $0 # y
loop:
	# is L or R
	lb $t0 0($s0)
	beq $t0 82 is_R
	beq $t0 76 is_L
	beq $t0 44 is_comma
	beq $t0 32 is_space
	beq $t0 10 solve_end
	beq $t0 0 solve_end
	j is_int
	
is_R:
	add $s1 $s1 2
is_L:
	add $s1 $s1 -1
	li $t0 4
	addi $s1 $s1 4
	div $s1 $t0
	mfhi $s1
is_comma:
is_space:
	j next_char

is_int:
	move $a0 $s0
	jal read_int
	move $s0 $a0
directions:
	#addi $v0 $v0 -1
	#ble $v0 -1 next_char
	beq $s1 0 north
	beq $s1 1 east
	beq $s1 2 south
	beq $s1 3 west
north:
	add $t7 $t7 $v0
	j directions_end
east:
	add $t6 $t6 $v0
	j directions_end
south:
	sub $t7 $t7 $v0
	j directions_end
west:
	sub $t6 $t6 $v0
	j directions_end

directions_end:

next_char:
	addi $s0 $s0 1
	j loop
	
solve_end:
	j solved
	
#code goes here
# read file
# split on commas, get L or R and atoi like
# make your python code tidier



read_int:
	# pass $a0 = memory location to start reading from
	# returns $a0 memory location stopped reading (not a digit)
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
	li $a2 600
	syscall
	jr $ra
	
	
        
program_end:
	li $v0 10
	syscall
