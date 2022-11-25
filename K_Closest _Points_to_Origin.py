class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        con = []
        for i in points:
            i.append(i[0]**2+i[1]**2)
            i.reverse()
            con.append(i)
        con.sort()
        result = []
        i = 0
        while k>0:
            a = con[i][1:]
            a.reverse()
            result.append(a)
            k-=1
            i+=1
        return result
