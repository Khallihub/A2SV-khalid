class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if s is None:
            return ""
        chars = set(s)

        idx = -1
        for i in range(len(s)):
            if  not (s[i].upper() in chars and s[i].lower() in chars):
                idx = i
                break
        else:
            return s
        
        left = self.longestNiceSubstring(s[:idx])
        right = self.longestNiceSubstring(s[idx+1:])


        if len(left) >= len(right):
            return left
        else:
            return right

