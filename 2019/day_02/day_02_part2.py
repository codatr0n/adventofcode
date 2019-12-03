# https://adventofcode.com/2019/day/2#part2

with open('input.txt', 'r') as file:
    int_codes = file.read().strip().split(',')

memory = [int(x) for x in int_codes]
memory[1] = 12
memory[2] = 2

search_for = 19690720
noun_max = 100
verb_max = 100


def search_mem(noun, verb, memory):
    memory[1] = noun
    memory[2] = verb

    for i in range(0, len(memory), 4):
        opcode, a, b, address = memory[i:i + 4]

        if (opcode == 99):
            return memory[0]

        if (opcode == 1):
            memory[address] = memory[a] + memory[b]

        if (opcode == 2):
            memory[address] = memory[a] * memory[b]

    return memory[0]


for noun in range(noun_max):
    for verb in range(verb_max):
        result = search_mem(noun, verb, memory[:])
        if (result == search_for):
            print(100 * noun + verb)

# result: 3892