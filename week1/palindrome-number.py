class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        nums = []
        while x > 0:
            nums.append(x%10)
            x //= 10
        temp = nums.copy()
        nums.reverse()
        if temp == nums:
            return True
        else:
            return False
            