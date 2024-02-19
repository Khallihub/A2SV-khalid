class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        idxs =  defaultdict(lambda : -1)
        stk = []
        for i in nums2:
            while stk and stk[-1] < i:
                top = stk.pop()
                idxs[top] = i
            stk.append(i)
        for i in range(len(nums1)):
            nums1[i] = idxs[nums1[i]]               
        return nums1