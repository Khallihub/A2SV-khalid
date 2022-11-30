class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        lst = []
        r = len(nums)-1
        for i in range (int((len(nums)/2))):
            lst.append([nums[i],nums[r]])
            r-=1
        for i in range (len(lst)):
            lst[i] = lst[i][0]+lst[i][1]
        return max(lst)
