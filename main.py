import numpy

# init
with open('output.txt', 'w') as file:
    file.write('_start:\n')

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
        file.write(com)


for i in finalLines:
    if str(i).isdigit():
        add('\tpush ' + i + '\n')
    elif str(i) in '+-*':
        pass
    elif str(i) == 'dup':
        add('\tpush %rax\n')
    elif str(i) == 'swap':
        add('\tpop %rax, %rdx\n\tpop %rax, %rcx\n\tpush $rdx\n\tpush %rcx\n')

# exit
add('\tret\n')
