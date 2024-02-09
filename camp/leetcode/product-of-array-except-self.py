class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a = len(nums) - 1
        product = 1
        postfix = []
        for i in range(a,-1,-1):
            product *= nums[i]
            postfix.append(product)
        postfix.reverse()
        prefix = 1
        for i in range(len(nums)-1):
            postfix[i] = postfix[i+1] * prefix
            prefix *= nums[i]
        postfix[-1] = prefix
        return postfix