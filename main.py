import os
import sys
import numpy

# command-line run with 1 argument
if len(sys.argv) > 1:
    inputFile = sys.argv[1]
else:
    inputFile = 'app.txt'
outputFile = inputFile.split('.')[0] + '.s'

# output file init
with open(outputFile, 'w') as file:
    file.write('\n'
               '.section .text\n'
               '.globl _start\n'
               '\n'
               '_start:\n')

finalLines = []
with open(inputFile) as file:
    lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace('\n', ' ')
        finalLines.append(lines[i].split())

finalLines = list(numpy.concatenate(finalLines).flat)
print(finalLines)


def add(com, endline='\n'):
    with open(outputFile, 'a') as file:
        file.write(com + endline)


def opers():
    add('\tpop %rdx\n''\tpop %rcx\n', endline='')

    match str(i):
        case '+':
            add('\tadd %rdx, %rcx\n', endline='')
        case '-':
            add('\tsub %rdx, %rcx\n', endline='')
        case '*':
            add('\timul %rdx, %rcx\n', endline='')
        case '/':
            add('\tdiv %rdx, %rcx\n', endline='')

    add('\tpush %rcx\n')


for i in finalLines:
    if str(i).isdigit():
        add('\tpush $' + i + '\n')
    elif str(i) in '+-*':
        opers()
    else:
        match str(i):
            case 'dup':
                add('\tpop %rdx\n'
                    '\tpush %rdx\n'
                    '\tpush %rdx\n')
            case 'swap':
                add('\tpop %rdx\n'
                    '\tpop %rcx\n'
                    '\tpush %rdx\n'
                    '\tpush %rcx\n')
            case 'drop':
                add('\tpop %rdx\n')


            # TODO check if any conflicts between operations use of registers

# TODO print : .s

# exit
add('\tmov $60, %rax\n'
    '\tpop %rdi\n'
    '\tsyscall\n')

# TODO os.system()
os.system('as -o ' + outputFile.split('.')[0] + '.o' + outputFile)
os.system('ld -o ' + outputFile.split('.')[0] + ' ' + outputFile.split('.')[0] + '.o')

