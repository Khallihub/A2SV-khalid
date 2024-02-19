class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stk = []
        res = [-1 for i in nums]
        n = len(nums)
        for i in range(2*n):
            while stk and nums[stk[-1]] < nums[i%n]:
                top = stk.pop()
                res[top] = nums[i%n]
            stk.append(i%n)
        return res