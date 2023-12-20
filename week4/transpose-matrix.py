class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transpose= []
        for i in range(len(matrix[0])):
            tmp = []
            for j in range(len(matrix)):
                print(j,i)
                tmp.append(matrix[j][i])
            transpose.append(tmp)
        return transpose