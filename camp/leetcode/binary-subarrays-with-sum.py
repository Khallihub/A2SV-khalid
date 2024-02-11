class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1
        runningSum = 0
        res = 0
        for i in range(len(nums)):
            runningSum += nums[i]
            if runningSum - goal in prefix:
                res += prefix[runningSum-goal]
            prefix[runningSum] += 1        
        return res