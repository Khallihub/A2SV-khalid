class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.Prefix1D = []
        self.Prefix2D = [[0 for i in range (len(matrix[0])+1)]]
        for i in range(len(matrix)):
            runningSum = 0
            temp = []
            for j in range(len(matrix[0])):
                runningSum += matrix[i][j]
                temp.append(runningSum)
            self.Prefix1D.append(temp)
        runningPrefix = [0 for i in matrix[0]]
        for i in range(len(self.Prefix1D)):
            for j in range(len(self.Prefix1D[0])):
                runningPrefix[j] += self.Prefix1D[i][j]
            self.Prefix2D.append([0,*runningPrefix])
        print(self.Prefix2D)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        topLeft = self.Prefix2D[row1][col1]
        topRight = self.Prefix2D[row1][col2+1]
        bottomLeft = self.Prefix2D[row2+1][col1]
        bottomRight = self.Prefix2D[row2+1][col2+1]
        return bottomRight - bottomLeft - topRight + topLeft

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)