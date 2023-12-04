class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        t = 0
        for i in range(len(points)-1):
            while True:
                print(points,t)
                if points[i][0] < points[i+1][0] and points[i][1] < points[i+1][1]:
                    t += min((points[i+1][0] - points[i][0]), (points[i+1][1] - points[i][1]))
                    points[i] = [points[i][0]+min((points[i+1][0] - points[i][0]), (points[i+1][1] - points[i][1])), points[i][1]+min((points[i+1][0] - points[i][0]), (points[i+1][1] - points[i][1]))]
                elif points[i][0] > points[i+1][0] and points[i][1] > points[i+1][1]:
                    t += min((points[i][0] - points[i+1][0]), (points[i][1] - points[i+1][1]))
                    points[i] = [points[i][0]+min((points[i+1][0] - points[i][0]), (points[i+1][1] - points[i][1])), points[i][1]+min((points[i+1][0] - points[i][0]), (points[i+1][1] - points[i][1]))]
                elif points[i][0] == points[i+1][0] and points[i][1] < points[i+1][1]:
                    t += (points[i+1][1]-points[i][1])
                    points[i] = [points[i][0], points[i][1]+(points[i+1][1]-points[i][1])]
                elif points[i][0] == points[i+1][0] and points[i][1] > points[i+1][1]:
                    t += (points[i][1]-points[i+1][1])
                    points[i] = [points[i][0], points[i][1]-(points[i][1]-points[i+1][1])]
                elif points[i][0] > points[i+1][0] and points[i][1] < points[i+1][1]:
                    t += min(abs(points[i][0]-points[i+1][0]),abs(points[i][1]-points[i+1][1]))
                    points[i] = [points[i][0]-min(abs(points[i][0]-points[i+1][0]),abs(points[i][1]-points[i+1][1])), points[i][1]+min(abs(points[i][0]-points[i+1][0]),abs(points[i][1]-points[i+1][1]))]
                elif points[i][0] < points[i+1][0] and points[i][1] > points[i+1][1]:
                    t += min(abs(points[i][0]-points[i+1][0]),abs(points[i][1]-points[i+1][1]))
                    points[i] = [points[i][0]+min(abs(points[i][0]-points[i+1][0]),abs(points[i][1]-points[i+1][1])), points[i][1]-min(abs(points[i][0]-points[i+1][0]),abs(points[i][1]-points[i+1][1]))]
                elif points[i][0] > points[i+1][0] and points[i][1] == points[i+1][1]:
                    t += (points[i][0]-points[i+1][0])
                    points[i] = [points[i][0]-(points[i][0]-points[i+1][0]), points[i][1]]
                elif points[i][0] < points[i+1][0] and points[i][1] == points[i+1][1]:
                    t += (points[i+1][0]-points[i][0])
                    points[i] = [points[i][0]+(points[i+1][0]-points[i][0]), points[i][1]]
                else:
                    break
        return t
                