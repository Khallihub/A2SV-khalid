class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_ = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                max_ = max(max_,count)
                count = 0
        max_ = max(max_,count)
        return max_
                