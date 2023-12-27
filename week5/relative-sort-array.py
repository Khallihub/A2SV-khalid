class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        cnt = Counter(arr1)
        res = []
        for i in arr2:
            cur = cnt[i]
            for j in range(cur):
                res.append(i)
            del cnt[i]
        tmp = []
        for i in cnt:
            cur = cnt[i]
            for j in range(cur):
                tmp.append(i)
        tmp.sort()
        for i in tmp:
            res.append(i)
        return res