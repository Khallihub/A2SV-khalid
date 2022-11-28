class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        for i ,j in enumerate(nums):
            nums[i] = int(j)
        nums.sort()
        nums.reverse()
        return str(nums[k-1])
