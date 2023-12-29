class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i, v in enumerate(nums):
            nums[i] = str(v)
        nums.sort(reverse=True)
        for j in range(len(nums)-1):
            i = j
            print(nums)
            while nums[i] + nums[i+1] < nums[i+1]+ nums[i] and i >= 0:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                i-=1
        return str(int("".join(nums)))