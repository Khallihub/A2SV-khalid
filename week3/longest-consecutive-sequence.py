class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        res = 0
        for i in nums:
            if not i - 1 in numsSet:
                length = 0
                while i + length in numsSet:
                    length += 1
                res = max(res, length)
        return res

            