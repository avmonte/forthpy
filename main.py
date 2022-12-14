import numpy

# TODO sys input

# init
with open('output.s', 'w') as file:
    file.write('\n.global _start\n\n_start:\n')

finalLines = []
with open('input.txt') as file:
    lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace('\n', ' ')
        finalLines.append(lines[i].split())

finalLines = list(numpy.concatenate(finalLines).flat)
print(finalLines)


def add(com, endline='\n'):
    with open('output.s', 'a') as file:
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

    add('\tpush %rcx\n')


for i in finalLines:
    if str(i).isdigit():
        add('\tpush $' + i + '\n')
    elif str(i) in '+-*':
        opers()
    elif str(i) == 'dup':
        add('\tpop %rdx\n'
            '\tpush %rdx\n'
            '\tpush %rdx\n')
    elif str(i) == 'swap':
        add('\tpop %rdx\n'
            '\tpop %rcx\n'
            '\tpush %rdx\n'
            '\tpush %rcx\n')

# TODO print : .s

# exit
add('\tret\n')

# TODO os.system()
