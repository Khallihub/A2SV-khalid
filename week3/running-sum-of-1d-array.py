class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum = 0
        res = []
        for i in nums:
            runningSum += i
            res.append(runningSum)
        return res