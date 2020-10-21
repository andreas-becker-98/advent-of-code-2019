# Copyright 2020 by Andreas Becker

# Global variables
welcome_text = "Advent of Code, Day X:"
farewell_text = "That's all folks!"

# Functions
def retrieve_module_masses():
	masses = []
	with open('input_one.txt') as file:
		for line in file:
			if line.endswith('\n'):
				line = line[:len(line)-1]
			masses.append(int(line))
	return masses

def calculate_required_fuel(module_mass):
	fuel_required = (module_mass // 3) - 2
	fuel_required += calculate_fuel_for_fuel(fuel_required)
	return fuel_required

def calculate_fuel_for_fuel(fuel_mass):
	additional_fuel = (fuel_mass // 3) - 2
	if additional_fuel > 0:
		additional_fuel += calculate_fuel_for_fuel(additional_fuel)
	elif additional_fuel < 0:
		return 0
	return additional_fuel

# Main body
print(welcome_text)

module_masses = retrieve_module_masses()

total_fuel_required = 0

for module_mass in module_masses:
	total_fuel_required += calculate_required_fuel(module_mass)

print("Total fuel required:", total_fuel_required)

print(farewell_text)