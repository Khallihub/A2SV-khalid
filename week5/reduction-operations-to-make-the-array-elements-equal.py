class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        ops = 0
        print(nums)
        for j in range(len(nums)-1):
            if nums[j] != nums[j+1]:
                ops += j+1
        return ops