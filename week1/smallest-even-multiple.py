class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n % 2 == 0:
            return n
        for i in range(n, n*2+1, n):
            if i % 2 == 0:
                return i