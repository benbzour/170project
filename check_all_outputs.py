#!/usr/bin/python

import glob

def processInput(input_file, output_file):
	fin = open(input_file, "r")
	fout = open(output_file, "r")

	num_wiz_in_input = int(fin.readline().split()[0])
	# input_wizard_set = set(fin.readline().split())
	num_constraints = int(fin.readline().split()[0])

	output_ordering = fout.readline().split()
	output_ordering_set = set(output_ordering)
	output_ordering_map = {k: v for v, k in enumerate(output_ordering)}


	if (len(output_ordering_set) != num_wiz_in_input):
		return "Input file has unique {} wizards, but output file has {}".format(num_wiz_in_input, len(output_ordering_set))

	if (len(output_ordering_set) != len(output_ordering)):
		return "The output ordering contains repeated wizards."

# if (input_wizard_set != output_ordering_set):
#     return "The output ordering contains wizards that are different from the ones in the input ordering."

# Counts how many constraints are satisfied.

	constraints_satisfied = 0
	constraints_failed = []
	for i in range(num_constraints):
    
		line_num = i + 4
		constraint = fin.readline().split()

		c = constraint # Creating an alias for easy reference
		m = output_ordering_map # Creating an alias for easy reference

		wiz_a = m[c[0]]
		wiz_b = m[c[1]]
		wiz_mid = m[c[2]]

		if (wiz_a < wiz_mid < wiz_b) or (wiz_b < wiz_mid < wiz_a):
			
			constraints_failed.append(c)
		else:
			
			constraints_satisfied += 1
	if constraints_failed == []:
		constraints_failed = "Great Success!"
	return constraints_satisfied, num_constraints, constraints_failed


input20_path = "./phase2_inputs/inputs20/*"
input35_path = "./phase2_inputs/inputs35/*"
input50_path = "./phase2_inputs/inputs50/*"
inputStaff_path = "./phase2_inputs/Staff_Inputs/*"


output_path = "./outputs/"

files20 = glob.glob(input20_path)
files35 = glob.glob(input35_path)
files50 = glob.glob(input50_path)
filesStaff = glob.glob(inputStaff_path)
i = 0


for file in files20:
	output_file = output_path + "output20_" + str(i) + ".out"
	print( "output20_" + str(i))
	print(processInput(file, output_file))
	i += 1

i = 0
for file in files35:
	output_file = output_path + "output35_" + str(i) + ".out"
	print( "output35_" + str(i))
	print(processInput(file, output_file))
	i += 1


i = 0
for file in files50:
	output_file = output_path + "output50_" + str(i) + ".out"
	print( "output50_" + str(i))
	print(processInput(file, output_file))
	i += 1


i = 100
for file in filesStaff:
	output_file = output_path + "staff_" + str(i) + ".out"
	print( "staff_" + str(i))
	print(processInput(file, output_file))
	i += 20
	if i == 420:
		i = 60






