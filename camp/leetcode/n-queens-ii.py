class Board:
    def __init__(self,size):
        self.board = [["." for i in range(size)] for i in range(size)]
        self.usedRows = set()
        self.usedCols = set()
        self.usedMainDiagonals = set()
        self.usedReverseDiagonals = set()
        self.size = size
    
    def isValid(self):
        if len(self.usedRows) == self.size: return True
        return False

    def getBoard(self):
        res = []
        for row in self.board:
            res.append("".join(row))
        return tuple(res)
    
    def place(self,i,j):
        if i in self.usedRows or j in self.usedCols or i-j in self.usedMainDiagonals or i+j in self.usedReverseDiagonals:
            return False
        self.board[i][j] = "Q"
        self.usedRows.add(i)
        self.usedCols.add(j)
        self.usedMainDiagonals.add(i-j)
        self.usedReverseDiagonals.add(i+j)
        return True
    
    def remove(self,i,j):
        if not (i in self.usedRows or j in self.usedCols or i-j in self.usedMainDiagonals or i+j in self.usedReverseDiagonals):
            return False
        self.board[i][j] = "."
        self.usedRows.remove(i)
        self.usedCols.remove(j)
        self.usedMainDiagonals.remove(i-j)
        self.usedReverseDiagonals.remove(i+j)
        return True

    def toString(self):
        print(self.board)


class Solution:
    def totalNQueens(self, n: int) -> int:
        board = Board(n)
        placements = set()

        def backtrack(row):
            if board.isValid():
                placements.add(board.getBoard())
                return
            if row >= n: return

            for col in range(n):
                if not board.place(row, col): continue
                backtrack(row+1)
                board.remove(row, col)

        backtrack(0)
        return len(placements)