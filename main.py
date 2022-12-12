finalLines = []
with open('input.txt', 'r') as file:
    lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace('\n', ' ')
        finalLines.append(lines[i].split())

print(finalLines)
with open('output.txt', 'w') as file:
    pass

