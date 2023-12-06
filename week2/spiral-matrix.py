class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        i = 0
        j = 0
        visited = set()
        res = []
        start_row = 0
        start_col = 0
        end_row = len(matrix)
        end_col = len(matrix[0])
        while len(visited) < len(matrix)*len(matrix[0]):
            print(res)
            while j < end_col:
                if (i,j) not in visited:
                    res.append(matrix[i][j])
                    visited.add((i,j))
                j += 1
            j -= 1
            while i < end_row:
                if (i,j) not in visited:
                    res.append(matrix[i][j])
                    visited.add((i,j))
                i += 1
            i -= 1
            while j >= 0:
                if (i,j) not in visited:
                    res.append(matrix[i][j])
                    visited.add((i,j))
                j -= 1
            j = start_col
            while i >= 0:
                if (i,j) not in visited:
                    res.append(matrix[i][j])
                    visited.add((i,j))
                i -= 1
            end_row -= 1
            end_col -= 1
            start_col += 1
            start_row += 1
            i = start_row
            j = start_col
        
        return res