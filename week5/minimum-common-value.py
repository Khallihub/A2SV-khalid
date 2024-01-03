class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        t,b = 0,0
        while t < len(nums1) and b < len(nums2):
            if nums1[t] == nums2[b]:
                return nums1[t]
            elif nums1[t] < nums2[b]:
                t += 1
            elif nums1[t] > nums2[b]:
                b += 1
        return -1
