def dynamic_rec(activity_list, activity, budget, dp):

    if budget <= 0 or activity >= len(activity_list):
        return (0, 0)

    if dp[activity][budget] != (-1, 0):
        return dp[activity][budget]

    skip = dynamic_rec(activity_list, activity+1, budget, dp)

    if budget < activity_list[activity].cost:
        dp[activity][budget] = skip
    else:
        new_value, new_cost = dynamic_rec(activity_list, activity+activity_list[activity].skip+1, budget - activity_list[activity].cost, dp)
        take = (activity_list[activity].value + new_value, new_cost - activity_list[activity].cost)
        dp[activity][budget] = max(skip, take)

    return dp[activity][budget]

def backtrack(activity_list, budget, dp):
    activity = 0
    current_budget = budget
    chosen_list = []

    while activity < len(activity_list):
        if activity+1 < len(activity_list):
            
            next_activity = activity+activity_list[activity].skip+1
            removed = current_budget-activity_list[activity].cost
            next_value, next_cost = dp[next_activity][removed] if next_activity < len(activity_list) and removed > 0 else (0, 0)
            if removed >= 0 and (activity_list[activity].value+next_value, next_cost-activity_list[activity].cost) == dp[activity][current_budget]:
                chosen_list.append(activity+1)
                current_budget -= activity_list[activity].cost
                activity = next_activity
            else:
                activity = activity+1
        else:
            if current_budget > 0 and dp[activity][current_budget] > (0, 0):
                chosen_list.append(activity+1)
                current_budget -= activity_list[activity].cost
            activity = activity+1

    return chosen_list, budget-current_budget

def dynamic(activity_list, budget):
    dp = [[]]
    for i in activity_list:
        for j in range(4):
            dp.append([])
        for k in range(budget+1):
            dp[i.num-1].append((-1, 0))

    max_value, reverse_cost = dynamic_rec(activity_list, 0, budget, dp)
    chosen_list, final_cost = backtrack(activity_list, budget, dp)
    
    return max_value, chosen_list, final_cost
