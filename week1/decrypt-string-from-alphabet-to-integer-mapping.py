class Solution:
    def freqAlphabets(self, s: str) -> str:
        res = ""
        i = 0
        while i < len(s):
            if i < len(s)-2 and s[i+2] == "#":
                res += str(chr(int(s[i:i+2])+96) )
                i += 3
            else:
                if s[i] == "#":
                    i += 1
                else:
                    res += str(chr(int(s[i])+96))
                    i += 1
        return res
