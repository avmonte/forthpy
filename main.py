import numpy

# init
with open('output.txt', 'w') as file:
    file.write('\n.global _start\n\n_start:\n')

finalLines = []
with open('input.txt') as file:
    lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace('\n', ' ')
        finalLines.append(lines[i].split())

finalLines = list(numpy.concatenate(finalLines).flat)
print(finalLines)


def add(com):
    with open('output.txt', 'a') as file:
        file.write(com + '\n')


for i in finalLines:
    if str(i).isdigit():
        add('\tpush ' + i + '\n')
    elif str(i) in '+':
        add('\tpop %rsp, %rdx\n'
            '\tpop %rsp, %rcx\n'
            '\tadd $rdx, %rcx\n'
            '\tpush %rcx\n')
    elif str(i) in '-':
        add('\tpop %rsp, %rdx\n'
            '\tpop %rsp, %rcx\n'
            '\tsub $rdx, %rcx\n'
            '\tpush %rcx\n')
    elif str(i) in '*':
        add('\tpop %rsp, %rdx\n'
            '\tpop %rsp, %rcx\n'
            '\timul $rdx, %rcx\n'
            '\tpush %rcx\n')
    elif str(i) == 'dup':
        add('\tpush %rsp\n')
    elif str(i) == 'swap':
        add('\tpop %rsp, %rdx\n'
            '\tpop %rsp, %rcx\n'
            '\tpush $rdx\n'
            '\tpush %rcx\n')

# exit
add('\tret\n')
