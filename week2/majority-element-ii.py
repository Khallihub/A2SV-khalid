class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)/3 
        cnt = Counter(nums)
        res = []
        for i in cnt:
            if cnt[i] > n:
                res.append(i)
        return res
        