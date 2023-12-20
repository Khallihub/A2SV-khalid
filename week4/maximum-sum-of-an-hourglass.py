class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        r = c = 0
        max_ = 0
        while r <= rows - 3:
            cur = 0
            for i in range(r,r+3):
                for j in range(c,c+3):
                    if i == r + 1 and j == c or i == r + 1 and j == c + 2:
                        continue
                    cur += grid[i][j]
            print("max_: ",max_)
            max_ = max(max_, cur)
            if c + 3 == cols:
                c = 0
                r += 1
            else:
                c += 1
        return max_

