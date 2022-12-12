finalLines = []
with open('input.txt') as file:
    lines = file.readlines()
    print(lines)
    for i in range(len(lines)):
        print(i)
        lines[i] = lines[i].replace('\n', ' ')
        finalLines.append(lines[i].split())

print(finalLines)
# with open('output.txt', 'w') as file:
#     pass

