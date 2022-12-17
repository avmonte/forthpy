import os
import sys
import numpy

commands = []


def append(com, endblock='\n'):
    with open(output_file, 'a') as file:
        file.write(com + endblock)


def operations(command):
    append('\tpop %rdx\n''\tpop %rcx\n', endblock='')

    match command:
        case '+':
            append('\tadd %rdx, %rcx\n', endblock='')
        case '-':
            append('\tsub %rdx, %rcx\n', endblock='')
        case '*':
            append('\timul %rdx, %rcx\n', endblock='')

    append('\tpush %rcx\n')


def identify_commands():
    global commands

    with open(input_file) as file:
        lines_raw = file.readlines()
        for i in range(len(lines_raw)):
            lines_raw[i] = lines_raw[i].replace('\n', ' ')
            commands.append(lines_raw[i].split())

    commands = list(numpy.concatenate(commands).flat)


def main():
    identify_commands()

    # output file init
    with open(output_file, 'w') as file:
        file.write('')
    if '.h' in commands:
        append('.fmt:\n'
               '\t.asciz "%d\\n"\n'
               '.text\n')
    append('\n'
           '.globl _start\n'
           '\n'
           '_start:\n')

    # checking the dictionary
    for i in commands:
        if str(i).isdigit():
            append('\tpush $' + i + '\n')
        elif str(i) in '+-*':
            operations(str(i))
        else:
            match str(i):
                case 'dup':
                    append('\tpop %rdx\n'
                           '\tpush %rdx\n'
                           '\tpush %rdx\n')
                case 'swap':
                    append('\tpop %rdx\n'
                           '\tpop %rcx\n'
                           '\tpush %rdx\n'
                           '\tpush %rcx\n')
                case 'drop':
                    append('\tpop %rdx\n')
                case '.h':
                    append('\tpop %rdx\n'
                           '\tmov %rdx, %rsi\n'
                           '\tpush %rdx\n'
                           '\txor %rax, %rax\n'
                           '\tmov $.fmt, %rdi\n'
                           '\tcall printf\n')

                # TODO print : .s

    # exit
    append('\tmov $60, %rax\n'
           '\tpop %rdi\n'
           '\tsyscall\n')


# command-line run with 1 argument
if len(sys.argv) > 1:
    input_file = sys.argv[1]
else:
    input_file = 'app.txt'
output_file = input_file.split('.')[0] + '.s'

# start
main()

# creation the executable
os.system('as -o ' + output_file.split('.')[0] + '.o ' + output_file)

extra = ''
if '.h' in commands:
    extra = ' -lc -dynamic-linker /lib64/ld-linux-x86-64.so.2'
os.system('ld -o ' + output_file.split('.')[0] + ' ' + output_file.split('.')[0] + '.o' + extra)
