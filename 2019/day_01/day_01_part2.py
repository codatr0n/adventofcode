# https://adventofcode.com/2019/day/1#part2

with open('input.txt') as input:
    module_mass = input.readlines()


def calc_fuel(mass):
    return (int(mass) // 3) - 2


def calc_fuel_for_fuel(fuel):
    while fuel > 6:
        result = calc_fuel(fuel)
        module_fuel.append(result)
        fuel = result


# module fuel = module mass // 3 - 2
module_fuel = list()
for mass in module_mass:
    fuel = calc_fuel(mass)
    module_fuel.append(fuel)
    calc_fuel_for_fuel(fuel)

result = sum(module_fuel)
print(result)
# 5142043