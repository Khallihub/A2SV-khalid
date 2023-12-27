class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = Counter(nums1)
        n2 = Counter(nums2)
        res = []
        for k,v in n1.items():
            if k in n2:
                for i in range(min(n1[k],n2[k])):
                    res.append(k)
        return res
