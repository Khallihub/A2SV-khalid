class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        cnt = 0
        left, right = 0, len(nums)-1
        while right > left:
            if nums[left] + nums[right] < target:
                cnt +=  right - left
                left += 1
            else:
                right -= 1
        return cnt