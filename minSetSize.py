class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = collections.Counter(arr)
        sorted(count.items(),key=lambda x:x[1])
        c = list(count.items())
        c.sort(key=lambda x:x[1],reverse=True)
        size = 0
        p = 0
        sss = 0
        while size < len(arr)/2:
            size+=c[p][1]
            p+=1
            sss += 1
        return sss
