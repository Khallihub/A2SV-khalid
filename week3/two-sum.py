class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        di = {}
        for i in range(len(nums)):
            if nums[i] in di:
                return [i, di[nums[i]]]
            di[target - nums[i]] = i
        
