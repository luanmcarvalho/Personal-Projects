class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        
        p1, p2, p3 = 1, 1, 0

        for i in range(3, n+1):
            current = p1 + p2 + p3
            p3 = p2
            p2 = p1
            p1 = current
        return p1