class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        rg = set(range(left,right+1))
        for i in range(len(ranges)):
            print(rg)
            rg = rg - set(range(ranges[i][0],(ranges[i][1])+1))
        if rg: return False
        else: return True