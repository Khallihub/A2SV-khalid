class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        sArr = list(s)
        left = 0
        right = k - 1
        i = 0
        while i < len(sArr):
            left = k*i*2
            right = min(left + k - 1, len(sArr) - 1)
            while left < len(sArr) and left < right :
                sArr[left], sArr[right] = sArr[right], sArr[left]
                right -= 1
                left += 1
            i += 1
        return "".join(sArr)