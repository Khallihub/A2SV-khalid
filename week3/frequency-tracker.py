class FrequencyTracker:

    def __init__(self):
        self.freq = defaultdict(int)
        self.vals = defaultdict(int)

    def add(self, number: int) -> None:
        freq = self.vals[number]
        self.freq[freq] -= 1
        self.freq[freq+1] += 1
        self.vals[number] += 1

    def deleteOne(self, number: int) -> None:
        freq = self.vals[number]
        if self.freq[freq]:
            self.freq[freq] -= 1
            self.freq[freq-1] += 1
        if self.vals[number]:
            self.vals[number] -= 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq[frequency]


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)