class Solution:
    def wateringPlants(self, plants: list[int], capacity: int) -> int:
        max_ = capacity
        steps = 0
        i = 0
        while i < len(plants):
            if plants[i] <= capacity:
                capacity -= plants[i]
                steps += 1
                i+=1
            else:
                steps += i*2
                capacity = max_
        return steps