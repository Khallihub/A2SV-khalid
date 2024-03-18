class TimeMap:

    def __init__(self):
        self.pairs = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.pairs[key].append([timestamp, value])
 
    def get(self, key: str, timestamp: int) -> str:
        cur = self.pairs[key]
        low, high = 0, len(cur)-1
        if high == -1:
            return ""
        while low < high:
            mid = (low+high)//2
            if cur[mid][0] >= timestamp:
                high = mid
            else:
                low = mid + 1
        if cur[low][0] > timestamp:
            if low == 0:
                return ""
            else:
                return cur[low-1][1]
        return cur[low][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)