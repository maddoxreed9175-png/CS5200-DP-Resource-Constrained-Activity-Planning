def dynamic_rec(activity_list, activity, budget, dp):
    if dp[activity][budget] != -1:
        return dp[activity][budget]

    if budget == 0 or activity+1 > len(activity_list):
        dp[activity][budget] = 0

    if budget < activity_list[activity].cost:
        dp[activity][budget] = dynamic_rec(activity_list, activity+1, budget, dp)

    if budget >= activity_list[activity].cost:
        dp[activity][budget] = max(dynamic_rec(activity_list, activity+activity_list[activity].skip+1, budget-activity_list[activity].cost, dp) + activity_list[activity].value, dynamic_rec(activity_list, activity+1, budget, dp))

    return dp[activity][budget]

def dynamic(activity_list, budget):
    dp = []
    for i in activity_list:
        dp.append([])
        for j in range(budget):
            dp[i].append(-1)

    return dynamic_rec(activity_list, 0, budget, dp)
