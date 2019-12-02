# https://adventofcode.com/2019/day/2

with open('input.txt', 'r') as file:
    int_codes = file.read().strip().split(',')

int_codes = [int(x) for x in int_codes]

int_codes[1] = 12
int_codes[2] = 2

for i in range(0, len(int_codes), 4):
    op, a, b, out = int_codes[i:i + 4]
    if op == 99:
        print('opcode 99 - halt')
        print('position 0 value is:', int_codes[0])
        break
    elif op == 1:
        result = int_codes[a] + int_codes[b]
        int_codes[out] = result
    elif op == 2:
        result = int_codes[a] * int_codes[b]
        int_codes[out] = result

# result is: 7210630