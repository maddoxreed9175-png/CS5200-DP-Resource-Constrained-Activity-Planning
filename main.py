import random

from dynamic_program import dynamic
from brute_program import brute
from activity_generator import generator

activities_to_generate = 100

activity_lists = generator(activities_to_generate)

num_correct = 0

for i in activity_lists:
    budget = random.randint(1, 20)
    
    brute_result = brute(i, budget)
    dynamic_result = dynamic(i, budget)
    if brute_result == dynamic_result:
        num_correct += 1
        print(".")
    else:
        print("Error: [")
        for j in i:
            print("A", j.num, ", Value = ", j.value, ", Cost = ", j.cost, ", Skip = ", j.skip, sep="")
        print("Budget =", budget)
        print("Brute Result =", brute_result)
        print("Dynamic Result =", dynamic_result)
        print("]")

print("Random validation tests passed: ", num_correct, " / ", activities_to_generate, sep="")
