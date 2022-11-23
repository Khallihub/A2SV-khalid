class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        lst = []
        for i in nums:
            x = 0
            for j in nums:
                if j < i:
                    x+=1
            lst.append(x)
        return lst
