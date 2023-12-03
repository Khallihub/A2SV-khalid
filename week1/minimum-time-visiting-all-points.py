class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        t = 0
        for i in range(len(points)-1):
            while True:
                if points[i][0] < points[i+1][0] and points[i][1] < points[i+1][1]:
                    points[i] = [points[i][0]+1, points[i][1]+1]
                elif points[i][0] > points[i+1][0] and points[i][1] > points[i+1][1]:
                    points[i] = [points[i][0]-1, points[i][1]-1]
                elif points[i][0] == points[i+1][0] and points[i][1] < points[i+1][1]:
                    points[i] = [points[i][0], points[i][1]+1]
                elif points[i][0] > points[i+1][0] and points[i][1] < points[i+1][1]:
                    points[i] = [points[i][0]-1, points[i][1]+1]
                elif points[i][0] < points[i+1][0] and points[i][1] > points[i+1][1]:
                    points[i] = [points[i][0]+1, points[i][1]-1]
                elif points[i][0] == points[i+1][0] and points[i][1] > points[i+1][1]:
                    points[i] = [points[i][0], points[i][1]-1]
                elif points[i][0] > points[i+1][0] and points[i][1] == points[i+1][1]:
                    points[i] = [points[i][0]-1, points[i][1]]
                elif points[i][0] < points[i+1][0] and points[i][1] == points[i+1][1]:
                    points[i] = [points[i][0]+1, points[i][1]]
                else:
                    break
                t += 1
        return t
                