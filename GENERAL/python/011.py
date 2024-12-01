class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 0:
            return 0
        elif n == 1:
            return cost[0]
        elif n == 2:
            return min(cost[0], cost[1])
        
        dp1, dp2 = cost[0], cost[1]
        for i in range(2, n):
            c = min(dp1 + cost[i], dp2 + cost[i])
            dp1, dp2 = dp2, c
        return min(dp1, dp2)
