class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        max_distance = max(trips, key=lambda x:x[2])[2]
        passengers = [0 for i in range(max_distance+1)]
        for trip in trips:
            passengers[trip[1]] += trip[0]
            if trip[2] + 1 <= max_distance:
                passengers[trip[2]] -= trip[0]
        runningSum = 0 
        for i in range(len(passengers)):
            runningSum += passengers[i]
            passengers[i] = runningSum
            if runningSum > capacity:
                return False
        return True
