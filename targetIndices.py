class Solution:
    def class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        result = []
        nums.sort()
        for i in nums:
            if i == target:
                result.append(nums.index(i))
                a = nums.index(i)
                nums[a] = "q"
        return result(self, nums: List[int], target: int) -> List[int]:
        result = []
        nums.sort()
        for i in nums:
            if i == target:
                result.append(nums.index(i))
                a = nums.index(i)
                nums[a] = "q"
        return result
