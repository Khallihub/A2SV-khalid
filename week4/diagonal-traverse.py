class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        cols = len(mat[0])
        ans  = []
        i = j = 0
        up = True
        while len(ans) < rows * cols:
            if up:
                while i >= 0 and j < cols:
                    ans.append(mat[i][j])
                    i -= 1
                    j += 1
                if j == cols:
                    j -= 1
                    i += 2
                else:
                    i += 1
                up = False
            else:
                while i < rows and j >= 0:
                    ans.append(mat[i][j])
                    i += 1
                    j -=1 
                if i == rows:
                    j += 2
                    i -= 1
                else:
                    j += 1
                up = True
        return ans