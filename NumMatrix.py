class NumMatrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.lst = [[0]*(len(self.matrix[0])+1)]
        flag = False
        for row in range (len(self.matrix)):
            lstin = [0]
            sum = 0
            for column in range (len(self.matrix[row])):
                cur = self.matrix[row][column]
                sum += cur
                if flag == True:
                    above = self.lst[row][column+1]
                    sum += above
                lstin.append(sum)
                if flag == True:
                    sum -= above
            flag = True
            self.lst.append(lstin)
    def sumRegion(self, row1, col1, row2, col2):
        k = self.lst
        tl = k[row1][col1]
        br = k[row2+1][col2+1]
        bl1 = k[row2+1][col1]
        tr1 = k[row1][col2+1]
        sum = br - tr1 - bl1 + tl
        return sum
        

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
