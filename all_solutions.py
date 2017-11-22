import argparse
from output_validator import processInput
from solver import solve

def all_sols(input_filename, output_filename):
    #read input
    with open(input_filename) as f:
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
    solution, failed_constraints = solve(num_wizards, num_constraints, wizards, constraints)

    #write output
    with open(output_filename, "w") as f:
        for wizard in solution:
            f.write("{0} ".format(wizard))
    
    return solution, failed_constraints

    

def main():
    twenties = ["input20_0.in", "input20_1.in", "input20_2.in", "input20_3.in", "input20_4.in", "input20_5.in", "input20_6.in", "input20_7.in", "input20_8.in", "input20_9.in"]
    thirties = ["input35_0.in", "input35_1.in", "input35_2.in", "input35_3.in", "input35_4.in", "input35_5.in", "input35_6.in", "input35_7.in", "input35_8.in", "input35_9.in"]
    fifties = ["input50_0.in", "input50_1.in", "input50_2.in", "input50_3.in", "input50_4.in", "input50_5.in", "input50_6.in", "input50_7.in", "input50_8.in", "input50_9.in"]
    staff = ["staff_60.in", "staff_80.in", "staff_100.in", "staff_120.in", "staff_140.in",
            "staff_160.in", "staff_180.in", "staff_200.in", "staff_220.in", "staff_240.in",
            "staff_260.in", "staff_280.in", "staff_300.in", "staff_320.in", "staff_340.in",
            "staff_360.in", "staff_380.in", "staff_400.in"]
    twenties_out = ["output20_0.out", "output20_1.out", "output20_2.out", "output20_3.out", "output20_4.out", "output20_5.out", "output20_6.out", "output20_7.out", "output20_8.out", "output20_9.out"]
    thirties_out = ["output35_0.out", "output35_1.out", "output35_2.out", "output35_3.out", "output35_4.out", "output35_5.out", "output35_6.out", "output35_7.out", "output35_8.out", "output35_9.out"]
    fifties_out = ["output50_0.out", "output50_1.out", "output50_2.out", "output50_3.out", "output50_4.out", "output50_5.out", "output50_6.out", "output50_7.out", "output50_8.out", "output50_9.out"]
    staff_out = ["staff_60.out", "staff_80.out", "staff_100.out", "staff_120.out", "staff_140.out",
            "staff_160.out", "staff_180.out", "staff_200.out", "staff_220.out", "staff_240.out",
            "staff_260.out", "staff_280.out", "staff_300.out", "staff_320.out", "staff_340.out",
            "staff_360.out", "staff_380.out", "staff_400.out"]
    i = 0
    while i <= 10:
        sol, failed = all_sols(twenties[i], twenties_out[i])
        i+= 1
        print("The solution is:", sol, "and the number of failed constraints are:", failed)
    i = 0
    while i <= 10:
        sol, failed = all_sols(thirties[i], thirties_out[i])
        i+= 1
        print("The solution is:", sol, "and the number of failed constraints are:", failed)
    i = 0
    while i <= 10:
        sol, failed = all_sols(fifties[i], fifties_out[i])
        i+= 1
        print("The solution is:", sol, "and the number of failed constraints are:", failed)
    i = 0
    while i<= 18:
        sol, failed = all_sols(staff[i], staff_out[i])
        i+= 1
        print("The solution is:", sol, "and the number of failed constraints are:", failed)

if _name_ == "_main_":
    main()