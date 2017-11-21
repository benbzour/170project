import argparse
from itertools import permutations
# import ortools
# from ortools.constraint_solver import pywrapcp
import random
import copy
import math

"""
======================================================================
  Complete the following function.
======================================================================
"""

def solve(num_wizards, num_constraints, wizards, constraints):
    """
    Write your algorithm here.
    Input:
        num_wizards: Number of wizards
        num_constraints: Number of constraints
        wizards: An array of wizard names, in no particular order
        constraints: A 2D-array of constraints, 
                     where constraints[0] may take the form ['A', 'B', 'C']i

    Output:
        An array of wizard names in the ordering your algorithm returns
    """

    # print(num_wizards)
    # print(num_constraints)
    # print(wizards)
    # print(constraints)
    # node_set = set(wizards)
    


    def cost(sol,num_constraints,constraints):
        constraints_satisfied = 0
        constraints_failed = []
        output_ordering_map = {k: v for v, k in enumerate(sol)}
        for c in constraints:

            m = output_ordering_map # Creating an alias for easy reference

            wiz_a = m[c[0]]
            wiz_b = m[c[1]]
            wiz_mid = m[c[2]]

            if (wiz_a < wiz_mid < wiz_b) or (wiz_b < wiz_mid < wiz_a):
                constraints_failed.append(c)
            else:
                constraints_satisfied += 1
        return num_constraints - constraints_satisfied

    def neighbors(sol):
        wiz1 = random.randint(0,num_wizards-1)
        wiz2 = random.randint(0,num_wizards-1)

        new_sol = copy.copy(sol)
        temp = new_sol[wiz1]
        new_sol[wiz1] = new_sol[wiz2]
        new_sol[wiz2] = temp
        
        return new_sol

    def acceptance_probability(old_cost,new_cost,T):
        exponent = (old_cost - new_cost) / T
        
        try:
            ans = math.exp(exponent)
        except OverflowError:
            ans = float('inf')
        return ans


    def anneal(solution, num_constraints, constraints):
        old_cost = 0
        new_cost = 0
        old_cost = cost(solution,num_constraints,constraints)
        T = 1.0
        T_min = 0.000001
        alpha = 0.98
        while T > T_min:
            i = 1
            while i <= 1000:
                new_solution = neighbors(solution)
                new_cost = cost(new_solution,num_constraints,constraints)
                if new_cost == 0:
                    return new_solution,new_cost
                ap = acceptance_probability(old_cost, new_cost, T)
                if ap > random.random():
                    solution = new_solution
                    old_cost = new_cost
                i += 1
            T = T*alpha
        return solution, old_cost

    s = copy.copy(wizards)
    random.shuffle(s)
    ret = anneal(s,num_constraints,constraints)
    
    for i in range(10):
        if ret[1] == 0:
            break
        random.shuffle(s)
        new_ret = anneal(s,num_constraints,constraints)
        print(i)
        if new_ret[1] < ret[1]:
            ret = new_ret
    print("constraints failed: {0}".format(ret[1]))
    return ret[0]




"""
======================================================================
   No need to change any code below this line
======================================================================
"""

def read_input(filename):
    with open(filename) as f:
        num_wizards = int(f.readline())
        num_constraints = int(f.readline())
        constraints = []
        wizards = set()
        for _ in range(num_constraints):
            c = f.readline().split()
            constraints.append(c)
            for w in c:
                wizards.add(w)
                
    wizards = list(wizards)
    return num_wizards, num_constraints, wizards, constraints

def write_output(filename, solution):
    with open(filename, "w") as f:
        for wizard in solution:
            f.write("{0} ".format(wizard))

if __name__=="__main__":
    parser = argparse.ArgumentParser(description = "Constraint Solver.")
    parser.add_argument("input_file", type=str, help = "___.in")
    parser.add_argument("output_file", type=str, help = "___.out")
    args = parser.parse_args()

    num_wizards, num_constraints, wizards, constraints = read_input(args.input_file)
    solution = solve(num_wizards, num_constraints, wizards, constraints)
    write_output(args.output_file, solution)




