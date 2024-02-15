class Solution:
    def numberOfWays(self, s: str) -> int:
        zeros = 0
        ones = 0
        zoz = 0
        ozo = 0
        ans = 0
        for i in s:
            if i == "0":
                zeros += 1
                ozo += ones
                ans += zoz
            else:
                zoz += zeros
                ones += 1
                ans += ozo
        return ans
            