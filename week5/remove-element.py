class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left, right = 0,0
        ans = 0
        while right < len(nums):
            if nums[right] != val:
                nums[left], nums[right] = nums[right], nums[left]
                ans += 1
                left += 1
            right += 1
        return ans