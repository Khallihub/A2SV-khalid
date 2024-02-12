class Solution:
    def maxScore(self, s: str) -> int:
        ones = 0
        for i in range(1,len(s)):
            if s[i] == "1":
                ones += 1
        zeros = 0
        if s[0] == "0":
            zeros += 1
        output = 0
        for i in range(1, len(s)):
            output = max(output, ones + zeros)
            if s[i] == "0":
                zeros += 1
            else:
                ones -= 1
        return output          