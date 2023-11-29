class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        a = num//3
        for i in range(a - 10, a + 10):
            sum_  = (i )+ (i+1 )+ (i+2)
            if sum_ == num:
                return [i,i+1, i+2]
