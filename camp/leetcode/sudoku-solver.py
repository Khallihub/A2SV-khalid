class Sudoku:
    def __init__(self):
        self.rows = [set() for i in range(9)]
        self.rowVals = [set() for i in range(9)]
        self.cols = [set() for i in range(9)]
        self.colVals = [set() for i in range(9)]
        self.boxes = [set() for i in range(9)]
        self.boxVals = [set() for i in range(9)]
    
    def isValid(self):
        for row in self.rows:
            if len(row) != 9:
                return False
        return True

    def insert(self, val, i,j):
        
        idx = 0
        if i < 3 and j < 3:
            idx = 0
        elif i < 3 and j < 6:
            idx = 1
        elif i < 3 and j > 5:
            idx = 2

        elif i < 6 and j < 3:
            idx = 3
        elif i < 6 and j < 6:
            idx = 4
        elif i < 6 and j > 5:
            idx = 5
            
        elif i > 5 and j < 3:
            idx = 6
        elif i > 5 and j < 6:
            idx = 7
        elif i > 5 and j > 5:
            idx = 8

    
        if val in self.rowVals[i] or val in self.colVals[j] or val in self.boxVals[idx]:
            return False
        self.rows[i].add(tuple([i,j,val]))
        self.rowVals[i].add(val)
        self.cols[j].add(tuple([i,j,val]))
        self.colVals[j].add(val)
        self.boxes[idx].add(tuple([i,j,val]))
        self.boxVals[idx].add(val)
        return True

    def remove(self,val,i,j):
        idx = 0
        if i < 3 and j < 3:
            idx = 0
        elif i < 3 and j < 6:
            idx = 1
        elif i < 3 and j > 5:
            idx = 2

        elif i < 6 and j < 3:
            idx = 3
        elif i < 6 and j < 6:
            idx = 4
        elif i < 6 and j > 5:
            idx = 5
            
        elif i > 5 and j < 3:
            idx = 6
        elif i > 5 and j < 6:
            idx = 7
        elif i > 5 and j > 5:
            idx = 8

        if not (val in self.rowVals[i] or val in self.colVals[j] or val in self.boxVals[idx]):
            return False
        self.rows[i].remove(tuple([i,j,val]))
        self.rowVals[i].remove(val)
        self.cols[j].remove(tuple([i,j,val]))
        self.colVals[j].remove(val)
        self.boxes[idx].remove(tuple([i,j,val]))
        self.boxVals[idx].remove(val)
        return True

    def toString(self):
        for i in self.rows:
            print(i)

    def toArray(self, board):
        for row in self.rows:
            for element in row:
                board[element[0]][element[1]] = element[2]
        

class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        sudoku = Sudoku()
        empty = []
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    sudoku.insert(board[i][j],i,j)
                else:
                    empty.append([i,j])
        
        def backtrack(emptyIndex):
            if emptyIndex == len(empty) and sudoku.isValid():
                return True
            elif emptyIndex >= len(empty):
                return
            for i in range(1,10):
                tmp = sudoku.insert(str(i), empty[emptyIndex][0], empty[emptyIndex][1])
                if not tmp:
                    continue
                if backtrack(emptyIndex+1):
                    return True
                sudoku.remove(str(i), empty[emptyIndex][0], empty[emptyIndex][1])

        backtrack(0)
        sudoku.toArray(board)







