class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        int1 = 0
        len1 = len(num1)-1
        for dig in num1:
            count = 0
            while str(count) != dig:
                count += 1
            int1 += count * 10**len1
            len1 -= 1
        int2 = 0
        len2 = len(num2)-1
        for dig in num2:
            count = 0
            while str(count) != dig:
                count += 1
            int2 += count * 10**len2
            len2 -= 1
        print(int1)
        print(int2)
        return str(int1*int2)
            
            
