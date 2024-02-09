class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefs = defaultdict(int)
        prefs[0] = 1
        res = 0
        runningSum = 0
        for i in nums:
            runningSum += i
            if runningSum - k in prefs:
                res += prefs[runningSum - k]
            prefs[runningSum] += 1
        return res