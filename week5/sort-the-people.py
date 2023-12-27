class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for j in range(len(names)-1,0,-1):
            for i in range(len(names)-1,0,-1):
                if heights[i-1] <= heights[i]:
                    names[i], names[i-1] = names[i-1], names[i]
                    heights[i], heights[i-1] = heights[i-1], heights[i]
        return names