class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        a = [intervals[0]]
        for i , j in intervals[1:]:
            lastIn = a[-1][1]
            if i <= lastIn:
                a[-1][1] = max(lastIn,j)
            else:
                a.append([i,j])
        return a
