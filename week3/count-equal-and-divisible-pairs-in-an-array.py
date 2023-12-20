class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        pairs = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i < j and (i*j)%k == 0 and nums[i] == nums[j]:
                    pairs += 1
        return pairs