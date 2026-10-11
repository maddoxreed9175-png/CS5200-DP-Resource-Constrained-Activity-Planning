import random

#from dynamic_program import BLANK
from brute_program import brute
from activity_generator import generator

activity_lists = generator(1)

for i in activity_lists:
    budget = random.randint(1, 20)
    print("[")
    for j in i:
        print("A", j.num, ", Value = ", j.value, ", Cost = ", j.cost, ", Skip = ", j.skip, sep="")
    print("Budget =", budget)
    print("Brute Result =", brute(i, budget))
    print("]")
