class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        result = []
        i = 0
        j = len(nums)-1
        while (len(result)<(len(nums))):
            result.append(nums[i])
            i+=1   
            if i<=j:
                result.append(nums[j])
                j-=1
        return result
