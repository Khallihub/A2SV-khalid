class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0,len(s)-1
        while left < right:
            while left < len(s) and not (s[left].isdigit() or s[left].isalpha()):
                left += 1
            while right >= 0 and not (s[right].isdigit() or s[right].isalpha()):
                right -= 1
            if left < len(s) and right >= 0 and s[right].lower() == s[left].lower():
                left += 1
                right -= 1
            elif left < len(s) and right >= 0 and s[right].lower() != s[left].lower():
                return False
            else:
                return True
        return True