class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        def sum (arr):
            sum = 0
            for i in arr:
                sum += i
            return sum
        right = sum(nums[1:])
        left = 0
        ans = 0
        for i in range (len(nums)-1):
            if left == right:
                return i
            left += nums[i]
            if nums[i+1] >= 0:
                right -= abs(nums[i+1])
            elif nums[i+1] < 0:
                right += abs(nums[i+1])
            ans = i
        if left == right and len(nums) > 1:
            return ans+1
        elif left == right and len(nums) == 1:
            return 0
        return -1
