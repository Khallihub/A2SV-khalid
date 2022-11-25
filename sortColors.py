class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        result = []
        for i in nums:
            if i == 0:
                result.append(i)
        for i in nums:
            if i == 1:
                result.append(i)
        for i in nums:
            if i == 2:
                result.append(i)
        for i in range (len(nums)):
            nums[i] = result[i]
