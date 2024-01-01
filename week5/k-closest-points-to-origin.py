class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance (point):
            return math.sqrt(point[0]**2 + point[1]**2)
        for i in range(len(points)):
            dist = distance(points[i])
            points[i] = [*points[i], dist]
        points.sort(key=lambda x:x[2])
        for i in range(len(points)):
            points[i] = points[i][:2]
        return points[:k]
