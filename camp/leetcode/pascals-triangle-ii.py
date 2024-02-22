class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        cur = self.getRow(rowIndex-1)
        res = [1]
        for i in range(1,len(cur)):
            res.append(cur[i-1]+cur[i])
        res.append(1)
        return res