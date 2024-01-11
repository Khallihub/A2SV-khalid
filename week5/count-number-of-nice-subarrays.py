class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odd_cnt = 0
        nice = 0
        left, right = 0,0
        while right < len(nums):
            if nums[right] % 2 != 0:
                odd_cnt += 1
            while odd_cnt > k:
                nice += len(nums) - right
                if nums[left] % 2 != 0:
                    odd_cnt -= 1 
                left += 1
            right += 1
        tmp = nice
        odd_cnt = 0
        nice = 0
        left, right = 0,0
        while right < len(nums):
            if nums[right] % 2 != 0:
                odd_cnt += 1
            while odd_cnt >= k:
                nice += len(nums) - right
                if nums[left] % 2 != 0:
                    odd_cnt -= 1 
                left += 1
            right += 1
        return nice - tmp