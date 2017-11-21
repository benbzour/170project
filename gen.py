#!/bin/python

import random
import itertools
import time
import string
from itertools import permutations





l = 5
vals = []
# char = 'a'
char_counter = {}


i = 0
while i < l:
	# char = chr(ord(char)+1)

	letters = string.ascii_lowercase
   	char = ''.join(random.choice(letters) for i in range(1))
   	if char not in vals:
   		vals.append(char)
   		i += 1
   		char_counter[char] = 0




num_constraints = 500
limit = 500 // l
constraints = []
valid = dict()
i = 0 
for x in range(len(vals)):

	after = vals[x+1:]
	before = vals[:x]

	if len(after) != 0:
		if (after[0],after[len(after)-1],vals[x]) not in valid and (after[len(after)-1],after[0],vals[x]) not in valid:
			if after[0] != after[len(after)-1]:
				if char_counter[vals[x]] < limit:
					constraints.append([after[0],after[len(after)-1],vals[x]])
					valid[(after[0],after[len(after)-1],vals[x])] = 1
					char_counter[vals[x]] += 1



	if x != 0:
		if (before[0],before[x-1],vals[x]) not in valid and (before[x-1],before[0],vals[x]) not in valid:
			if before[0] != before[x-1]:
				if char_counter[vals[x]] < limit:
					constraints.append([before[0],before[x-1],vals[x]])
					valid[(before[0],before[x-1],vals[x])] = 1
					char_counter[vals[x]] += 1

for x in range(len(vals)):

	after = vals[x+1:]
	before = vals[:x]


	for y in after[::2]:
		for z in after[1::2]:
			if (y,z,vals[x]) not in valid and (z,y,vals[x]) not in valid:
				if y != z:
					if len(constraints) < 500:
						if char_counter[vals[x]] < limit:
							constraints.append([y,z,vals[x]])
							valid[(y,z,vals[x])] = 1
							valid[(z,y,vals[x])] = 1
							char_counter[vals[x]] += 1

	for y in before[::2]:
		for z in before[1::2]:
			if (y,z,vals[x]) not in valid and (z,y,vals[x]) not in valid:
				if y != z:
					if len(constraints) < 500:
						if char_counter[vals[x]] < limit:
							constraints.append([y,z,vals[x]])
							valid[(y,z,vals[x])] = 1
							valid[(z,y,vals[x])] = 1
							char_counter[vals[x]] += 1



# s =""

# print(len(vals))
# for i in vals:
# 	s += i 
# 	s += " "
# print(s)
# print(num_constraints)
# for i in constraints:
# 	print("{0} {1} {2}".format(i[0],i[1],i[2]))


count = 0
def helper(num_constraints, cons,s):

	node_set = set(s)
	node_map = {k: v for v, k in enumerate(s)}
	
	for i in range(num_constraints):

	    constraint = cons[i]
	    if (len(constraint) != 3):
	        # print("Each constraint must have 3 wizards. Line {} (1-index) does not contain 3 wizards".format(i))
	    	return 0
	    if not set(constraint).issubset(node_set):
	        # print("Some of the wizards in line {} are not present in the perfect age ordering.".format(i))
	        return 0

	    wiz_a = node_map[constraint[0]]
	    wiz_b = node_map[constraint[1]]
	    wiz_mid = node_map[constraint[2]]

	    if (wiz_a < wiz_mid < wiz_b) or (wiz_b < wiz_mid < wiz_a):
	        # print("In line {i}, you said {wizard_mid}'s age was NOT in between {wizard_a} and {wizard_b}'s, however, in your optimal ordering, {wizard_a} appeared at {a_order}, {wizard_b} appeared at {b_order}, {wizard_mid} appeared at {mid_order}".format(i = i, wizard_a = constraint[0], wizard_b = constraint[1], wizard_mid = constraint[2], a_order = wiz_a, b_order = wiz_b, mid_order = wiz_mid))
	        return 0
	return 1


# combs = permutations(vals,l)
# for c in combs:
	
# 	start_time = time.time()
# 	k = helper(16,constraints,c)
# 	elapsed_time = time.time() - start_time
# 	if k != 0:
# 		order = c
# 	count += k


# print(count)
# s =""

# print(len(vals))
# for i in vals:
# 	s += i 
# 	s += " "
# print(s)
# print(num_constraints)
# for i in constraints:
# 	print("{0} {1} {2}".format(i[0],i[1],i[2]))

