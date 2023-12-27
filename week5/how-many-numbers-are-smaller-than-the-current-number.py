class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        cnt = [0]*101
        for i in range(len(nums)):
            cnt[nums[i]] += 1
        prefix = 0
        for i in range(len(cnt)):
            prefix += cnt[i]
            cnt[i] = prefix - cnt[i]
        res = []
        for i in nums:
            res.append(cnt[i])
        return res


