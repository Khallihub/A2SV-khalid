class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_ = -1
        for i in range(len(num)-2):
            if num[i] == num[i+1] == num[i+2]:
                max_ = max(int(num[i:i+3]),max_)
        if max_ == 0:
            return "000"
        elif max_ == -1:
            return ""
        return str(max_)