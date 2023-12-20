class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        cols = 0
        for i in range(len(strs[0])):
            for j in range(len(strs)-1):
                print(i,j)
                if ord(strs[j][i]) > ord(strs[j+1][i]):
                    cols += 1
                    break
        return cols