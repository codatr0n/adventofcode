# https://adventofcode.com/2019/day/1

with open('input.txt') as input:
    module_mass = input.readlines()


def calc_fuel(mass):
    return (int(mass) // 3) - 2


# module fuel = module mass // 3 - 2
module_fuel = list()
for mass in module_mass:
    fuel = calc_fuel(mass)
    module_fuel.append(fuel)

result = sum(module_fuel)
print(result)
# 3429947