def dynamic_rec(activity_list, activity, budget, dp):

    if budget <= 0 or activity >= len(activity_list):
        return 0

    if dp[activity][budget] != -1:
        return dp[activity][budget]

    if budget < activity_list[activity].cost:
        dp[activity][budget] = dynamic_rec(activity_list, activity+1, budget, dp)

    if budget >= activity_list[activity].cost:
        pick = dynamic_rec(activity_list, activity+activity_list[activity].skip+1, budget-activity_list[activity].cost, dp) + activity_list[activity].value
        dp[activity][budget] = max(pick, dynamic_rec(activity_list, activity+1, budget, dp))

    return dp[activity][budget]

def backtrack(activity_list, budget, dp):
    activity = 0
    current_budget = budget
    chosen_list = []
    while current_budget > 0 and activity < len(activity_list):
        if activity+1 < len(activity_list):
            if dp[activity][current_budget] > dp[activity+1][current_budget]:
                chosen_list.append(activity+1)
                current_budget -= activity_list[activity].cost
                activity = activity+activity_list[activity].skip+1
            else:
                activity = activity+1
        else:
            if current_budget >= activity_list[activity].cost:
                chosen_list.append(activity+1)
                current_budget -= activity_list[activity].cost
                activity = activity+1
            break

    return chosen_list, budget-current_budget

def dynamic(activity_list, budget):
    dp = [[]]
    for i in activity_list:
        for j in range(4):
            dp.append([])
        for k in range(budget+1):
            dp[i.num-1].append(-1)

    max_value = dynamic_rec(activity_list, 0, budget, dp)
    chosen_list = backtrack(activity_list, budget, dp)
    return chosen_list, max_value
