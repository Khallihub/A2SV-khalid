class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        distinct = len(set(nums))
        left, right = 0, 0
        win = defaultdict(int)
        res = 0
        while right < len(nums):
            win[nums[right]] += 1
            while len(win) == distinct:
                res += len(nums) - right
                win[nums[left]] -= 1 
                if win[nums[left]] == 0:
                    del win[nums[left]] 
                left += 1
            right += 1
        return res


            