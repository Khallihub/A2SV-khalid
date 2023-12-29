class Solution:
    def smallestNumber(self, num: int) -> int:
        if len(list(str(num))) == 1:
            return num
        if num >= 0:
            num = list(str(num))
            num.sort()
            idx = 0
            while idx < len(num):
                if num[idx] != "0":
                    break
                idx += 1
            num[0], num[idx] = num[idx], num[0]
            num = "".join(num)
        else:
            num = list(str(num))
            num.sort(reverse=True)
            num = num[:-1]
            num = "".join(num)
            num = "-" + num
        return int(num)
