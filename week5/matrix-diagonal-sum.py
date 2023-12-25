class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res = 0
        i,j = 0,0
        while i < len(mat) and j < len(mat):
            res += mat[i][j]
            i += 1
            j += 1
        i,j = 0,len(mat)-1
        while i < len(mat) and j >= 0:
            print(mat[i][j])
            if i == len(mat)//2 and j == len(mat)//2:
                i += 1
                j -= 1
                continue
            res += mat[i][j]
            i += 1
            j -= 1
        return res
