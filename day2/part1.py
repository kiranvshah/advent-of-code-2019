with open('input.txt') as file:
    codes = [int(code) for code in file.read().split(',')]

def opcode_1(a, b, c):
    codes[codes[c]] = codes[codes[a]] + codes[codes[b]]

def opcode_2(a, b, c):
    codes[codes[c]] = codes[codes[a]] * codes[codes[b]]

codes[1] = 12
codes[2] = 2

for position in range(0, len(codes), 4):
    opcode = codes[position]
    if opcode == 99:
        break
    if opcode == 1:
        opcode_1(position+1, position+2, position+3)
    elif opcode == 2:
        opcode_2(position+1, position+2, position+3)

print(codes[0])
