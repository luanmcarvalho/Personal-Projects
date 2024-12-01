class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        
        start1, start2 = 1,0        
        for i in range(2, n+1):
            current = start1 + start2
            start2 = start1
            start1 = current
        return start1
