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
            # removing comments
            for j in range(len(lines_raw[i])):
                if lines_raw[i][j] == '\\':
                    lines_raw[i] = lines_raw[i][:j]
                    break
            # removing \n \t and spaces
            commands.append(lines_raw[i].split())

    commands = list(numpy.concatenate(commands).flat)


def create_exe():
    # creating the executable
    output_file_name = output_file.split('.')[0]
    os.system(f"as -o {output_file_name}.o {output_file}")
    extra = ''
    if '.' in commands:
        extra = ' -lc -dynamic-linker /lib64/ld-linux-x86-64.so.2'
    os.system(f"ld -o {output_file_name} {output_file_name}.o{extra}")

    # cleaning up the folder, separating object and assembly files to a raw data folder
    os.system(f"rm -r {output_file_name}_raw")  # TODO error raised when folder does not exist
    os.system(f"mkdir {output_file_name}_raw")
    os.rename(f"{output_file_name}.o", f"{output_file_name}_raw/{output_file_name}.o")
    os.rename(f"{output_file_name}.s", f"{output_file_name}_raw/{output_file_name}.s")


def main():
    identify_commands()

    # OUTPUT FILE INIT
    # zeroing out the file in case if it already exists
    with open(output_file, 'w') as file:
        file.write('')

    # file header
    if '.' in commands:
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
        elif str(i) in ['/', 'mod']:
            append('\tpop %rcx\n'
                   '\tpop %rax\n'
                   '\tcqo\n'
                   '\tidiv %rcx\n', endblock='')
            if str(i) == '/':
                append('\tpush %rax\n')
            else:
                append('\tpush %rdx\n')
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
                case '.':
                    append('\tpop %rdx\n'
                           '\tmov %rdx, %rsi\n'
                           '\tpush %rdx\n'
                           '\txor %rax, %rax\n'
                           '\tmov $.fmt, %rdi\n'
                           '\tcall printf\n')
                case _:
                    os.system(f"rm {output_file}")
                    print(f"Invalid syntax: '{str(i)}'")
                    return False

    # exit instructions
    append('\tmov $60, %rax\n'
           '\tpop %rdi\n'
           '\tsyscall\n')

    return True


# command-line run with 1 argument
if len(sys.argv) > 1:
    input_file = sys.argv[1]
else:
    input_file = 'app.fs'
output_file = input_file.split('.')[0] + '.s'

# start
if main():
    # create exe and clean up the folder
    create_exe()
