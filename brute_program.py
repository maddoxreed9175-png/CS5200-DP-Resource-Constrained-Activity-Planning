from itertools import chain, combinations

def powerset(iterable):
    s = list(iterable)
    #return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
    return [list(sub) for r in range(len(s) + 1) for sub in combinations(s, r)]

def brute(activity_list, budget):
    sets = list(powerset(activity_list))

    max_value = 0
    best_set = []
    best_cost = 0
    for combo in sets:
        total_cost = 0
        skip_violation = False
        current_skip = 0
        for activity in combo:
            total_cost += activity.cost
            if activity.num <= current_skip:
                skip_violation = True
                break
            current_skip = activity.num + activity.skip
        if total_cost <= budget and skip_violation == False:
            current_value = 0
            for activity in combo:
                current_value += activity.value

            if (current_value > max_value or (current_value == max_value and total_cost < best_cost) or (current_value == max_value and total_cost == best_cost and [a.num for a in combo] < [a.num for a in best_set])):
                max_value = current_value
                best_set = combo
                best_cost = total_cost
    printable_set = []
    for i in best_set:
        printable_set.append(i.num)
    return max_value, printable_set, best_cost

