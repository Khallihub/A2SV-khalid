class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0
        for i in range(n):
            week = i//7
            total += week + i%7 + 1
        return total

# 1 2 3 4 5 6 7 = 28
# 2 3 4 5 6 7 8 = 35
# 3 4 5 6 7 8 9 = 42