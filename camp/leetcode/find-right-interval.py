class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        res = [-1 for i in range(len(intervals) )] 
        for i in range(len(intervals)):
            intervals[i] = [*intervals[i],i]
        intervals.sort()
        for i in range(len(intervals)):
            cur = intervals[i]
            low, high = 0, len(intervals)-1
            while low < high:
                mid = (low + high)//2
                if intervals[mid][0] >= cur[1]:
                    high = mid
                else:
                    low = mid+1
            rightInterval = intervals[low]
            if rightInterval[0] >= cur[1]:            
                res[cur[2]] =  rightInterval[2]
        return res