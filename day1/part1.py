total = 0

with open('input.txt') as file:
    contents = file.read().split('\n')

for line in contents:
    total += int(line) // 3 - 2

print(total)