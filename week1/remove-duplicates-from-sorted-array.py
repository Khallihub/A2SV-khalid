class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cn = Counter(nums)
        for i in range(len(nums)):
            if cn[nums[i]] > 1:
                cn[nums[i]] -= 1
                nums[i] = "_"
        i,j = 0 ,0
        while j < len(nums):
            if nums[j] != "_":
                nums[i],nums[j] = nums[j], nums[i]
                j += 1 
                i += 1
            else:
                j += 1
        return len(cn)
    