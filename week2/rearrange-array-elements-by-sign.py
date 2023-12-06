class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p = []
        n = []
        for  i in nums:
            if i > 0:
                p.append(i)
            else:
                n.append(i)
        i = 0
        j = 0
        k = 0
        while i < len(nums):
            nums[i] = p[j]
            j += 1
            i += 1
            nums[i] = n[k]
            k += 1
            i += 1
        return nums