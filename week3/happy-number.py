class Solution:
    def isHappy(self, n: int) -> bool:
        def addSquares(lst):
            res = 0
            for i in lst:
                res += i**2
            return res
        visited = set()
        while True:
            nums = list(map(int,list(str(n))))
            if "".join(map(str,nums)) in visited:
                return False
            if addSquares(nums) == 1:
                return True
            visited.add("".join(map(str,nums)))
            n = addSquares(nums)
        
