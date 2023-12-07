class Solution:
    def largestOddNumber(self, num: str) -> str:
        largestOdd = ""
        for i in range(len(num)-1,-1,-1):
            print(num[i])
            if int(num[i]) % 2 != 0:
                largestOdd = num[0:i+1]
                break
        return largestOdd


        