class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for i in nums1:
            a = nums2.index(i)
            v = False
            for l in (nums2[a:]):
                if l > i:
                    ans.append(l)
                    v = True
                    break
            if not v:
                ans.append(-1)
        return ans
