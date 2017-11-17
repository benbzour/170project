#!/bin/python

import random
import itertools
import time
from itertools import permutations

a1 = []
a2 = []

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



	vals = []
	char = 'a'
	best_order = []
	best_constraints = []

	## vars to change ##
	l = 10
	num_constraints = 500

	for i in range(l):
		vals.append(char)
		char = chr(ord(char)+1)

	#generate a random order. 



	# print(node_map)
	# print(node_set)
	combs = permutations(vals,l)
	min_count = float('inf')
	data = []
	constraints = list()

	# for _ in range(10):
	count = 0

	t = float('inf')
	i = 0
	# while i < num_constraints:
	# 	w1 = random.choice(vals)
	# 	w2 = random.choice(vals)
	# 	w3 = random.choice(vals)
	# 	# if [w1,w2,w3] not in constraints:
	# 	constraints.append([w1,w2,w3])
	# 	i += 1

	print(constraints)

	# for c in combs:
		
	# 	start_time = time.time()
	# 	k = helper(num_constraints,constraints,c)
	# 	elapsed_time = time.time() - start_time
	# 	if k != 0:
	# 		order = c
	# 	count += k


	# data += [(num_constraints,count,elapsed_time)]


	# if count < min_count and count != 0:
	# 	best_order = order
	# 	best_constraints = constraints
	# 	min_count = count
	# 	best_t = t
	# constraints = []


	# if min_count < 5:

	s =""

	print(len(vals))
	for i in best_order:
		s += i 
		s += " "
	print(s)
	print(num_constraints)
	for i in best_constraints:
		print("{0} {1} {2}".format(i[0],i[1],i[2]))

	print("best count", min_count )

# 	for d in data:
# 		if d[1] != 0:
# 			a1.append(d[1])
# 		# 	print(d[1])
# 	for d in data:
# 		if d[1] != 0:
# 			a2.append(d[2])
# 			# print(d[2])


# for i in a1:
# 	print i

# for i in a2:
# 	print i
