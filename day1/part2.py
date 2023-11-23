total = 0

with open('input.txt') as file:
    contents = file.read().split('\n')

for line in contents:
    subtotal = 0
    last = int(line)
    while last > 0:
        last = last // 3 - 2
        if last > 0:
            subtotal += last
    total += subtotal

print(total)
