class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt = Counter(s)
        length = 0
        flag = False
        for i,v in cnt.items():
            if v%2 == 0:
                length += v
            else:
                length += v-1
                flag = True
        return length + flag