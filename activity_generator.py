import random

class Activity:

    def __init__(self, value, cost, skip, num):
        self.value = value
        self.cost = cost
        self.skip = skip
        self.num = num

def generator(num_to_generate):

    activity_lists = []

    for i in range(num_to_generate):

        activity_lists.append([]);
        num_elems = random.randint(1,20)
        
        for n in range(num_elems):
            new_activity = Activity(random.randint(1, 20), random.randint(1, 10), random.randint(0, 3), n+1)
            activity_lists[i].append(new_activity)

    return activity_lists
