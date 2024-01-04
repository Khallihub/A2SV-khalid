class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = set()
        for i in range(len(nums)):
            left, right = i, len(nums)-1
            while left < right:
                if i != left and i != right and nums[left] + nums[right] == nums[i]*-1:
                    cur = [nums[left], nums[i],nums[right]]
                    cur.sort()
                    cur = tuple(cur)
                    if not cur in triplets:
                        triplets.add(cur)
                    left += 1
                elif i != left and i != right and nums[left] + nums[right] > nums[i]*-1:
                    right -= 1
                elif i != left and i != right and nums[left] + nums[right] < nums[i]*-1:
                    left += 1
                elif left == i:
                    left += 1
                elif right == i:
                    right -= 1
        return triplets
