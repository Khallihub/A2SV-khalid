class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = set(nums)
        print(nums)
        for i in range(len(nums)+1):
            if not i in nums:
                return i        
