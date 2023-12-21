class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float("inf")
        for third in nums:
            if third > second:
                return True
            if third < first:
                first = third
            if third > first:
                second = third   
        return False 
                        