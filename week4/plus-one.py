class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        one = 1
        for i in range(len(digits)-1,-1,-1):
            digits[i] += one + carry
            one = 0
            carry = 0
            if digits[i] > 9:
                carry = 1
                digits[i] = 0
        if carry:
            digits.insert(0, 1)
        return digits