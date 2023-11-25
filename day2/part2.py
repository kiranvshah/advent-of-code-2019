from icecream import ic

with open('input.txt') as file:
    original_codes = [int(code) for code in file.read().split(',')]

target_result = 19690720

def opcode_1(array, a, b, c):
    array[array[c]] = array[array[a]] + array[array[b]]

def opcode_2(array, a, b, c):
    array[array[c]] = array[array[a]] * array[array[b]]

for noun in range(0, 100):
    for verb in range(0, 100):
        codes = original_codes.copy()
        codes[1] = noun
        codes[2] = verb

        for pos in range(0, len(codes), 4):
            opcode = codes[pos]
            if opcode == 99:
                break
            if opcode == 1:
                opcode_1(codes, pos+1, pos+2, pos+3)
            elif opcode == 2:
                opcode_2(codes, pos+1, pos+2, pos+3)

        output = codes[0]
        if output == target_result:
            print(100 * noun + verb)
            exit()
