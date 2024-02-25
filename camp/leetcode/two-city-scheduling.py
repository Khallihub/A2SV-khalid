class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[0] - x[1])
       
        cityA = sum(x[0] for x in costs[:len(costs)//2])
        cityB = sum(x[1] for x in costs[len(costs)//2:])
        
        return cityA + cityB
