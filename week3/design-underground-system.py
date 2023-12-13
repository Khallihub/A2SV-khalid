class UndergroundSystem:

    def __init__(self):
        self.checkIns = defaultdict(list)
        self.avgTime = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkIns[id] = [stationName, t] 

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation = self.checkIns[id][0]
        startTime = self.checkIns[id][1]
        self.avgTime[f"{startStation}*{stationName}"].append(t - startTime)
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        totalTime = sum(self.avgTime[f"{startStation}*{endStation}"])
        trips = len(self.avgTime[f"{startStation}*{endStation}"])
        return totalTime/trips
            
             


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)