class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        l = len(arr)
        def flip(i,arr):
            arr = arr[:i+1][::-1] + arr[i+1:]
            return arr
        r = l
        for _ in range(r):
            idx = arr.index(l)
            arr = flip(idx,arr)
            arr = flip(l-1,arr)
            res.append(idx+1)
            res.append(l)
            l-=1
        return res