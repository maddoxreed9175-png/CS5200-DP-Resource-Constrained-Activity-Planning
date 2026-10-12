import random

from dynamic_program import dynamic
from brute_program import brute
from activity_generator import generator

activities_to_generate = 100

activity_lists = generator(activities_to_generate)

num_correct = 0
counter = 0

for i in activity_lists:
    budget = random.randint(1, 20)
    
    brute_value, brute_list, brute_cost = brute(i, budget)
    dynamic_value, dynamic_list, dynamic_cost = dynamic(i, budget)
    counter += 1
    if brute_value == dynamic_value and brute_list == dynamic_list and brute_cost == dynamic_cost:
        num_correct += 1
        print("Test", counter, "passed")
    else:
        print("Error:\nInput=[")
        for j in i:
            print("A", j.num, ", Value = ", j.value, ", Cost = ", j.cost, ", Skip = ", j.skip, sep="")
        print("]")
        print("Budget =", budget)
        print("Dynamic Result:")
        print("Maximum value:", dynamic_value, "\nSelected activities:", dynamic_list, "\nTotal cost:", dynamic_cost)
        print("Brute Result:")
        print("Maximum value:", brute_value, "\nSelected activities:", brute_list, "\nTotal cost:", brute_cost, "\n")

print("Random validation tests passed: ", num_correct, " / ", activities_to_generate, sep="")
