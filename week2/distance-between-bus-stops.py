class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        total = 0
        for i in range(min(start,destination), max(start,destination)):
            total += distance[i]
        return min(total, sum(distance)-total)