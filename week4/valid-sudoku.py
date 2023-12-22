class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # horizontal
        for i in range(9):
            curRow = set()
            for j in range(9):
                if board[i][j] in curRow and board[i][j].isdigit():
                    return False
                curRow.add(board[i][j])
        for i in range(9):
            curCol = set()
            for j in range(9):
                if board[j][i] in curCol and board[j][i].isdigit():
                    return False
                curCol.add(board[j][i])
        i = 0
        j = 0
        while i <= 6 and j <= 6:
            threeBythree = set()
            print(i,j)
            for k in range(3):
                for l in range(3):
                    if board[i+k][j+l] in threeBythree and board[i+k][j+l].isdigit():
                        return False
                    threeBythree.add(board[i+k][j+l])
            print(threeBythree)
            if i >= 6:
                i = 0
                j += 3
            else:
                i += 3
        return True


            
