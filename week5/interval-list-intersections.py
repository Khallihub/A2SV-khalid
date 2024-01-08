class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        def findIntersection(ivls):
            # [[a,b],[c,d]]
            print(ivls)
            ivls.sort()
            if ivls[0][0] <= ivls[1][0] and ivls[0][1] >= ivls[1][1]:
                return ivls[1]
            if ivls[0][1] >= ivls[1][0]:
                return [ivls[1][0],ivls[0][1]]

        first = second = 0
        intersections = []
        while first < len(firstList) and second < len(secondList):
            intersection = findIntersection([firstList[first], secondList[second]])
            if intersection:
                intersections.append(intersection)
            if firstList[first][1] > secondList[second][1]:
                if second + 1 < len(secondList):
                    second += 1
                else:
                    first += 1
            else:
                if first + 1 < len(firstList):
                    first += 1
                else:
                    second += 1
        return intersections