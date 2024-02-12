class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        frequencies = [0] *( max(requests, key=lambda x:x[1])[1]+1)
        for request in requests:
            frequencies[request[0]] += 1
            if request[1] + 1 < len(frequencies):
                frequencies[request[1]+1] -= 1
        runningSum = 0
        prefix = []
        for i in range(len(frequencies)):
            runningSum += frequencies[i]
            prefix.append(runningSum)
        nums.sort(reverse=True)
        for i in range(len(prefix)):
            prefix[i] = [prefix[i], i]
        prefix.sort(reverse=True)
        sortedFreq = [None for i in range(len(nums))]
        k = 0
        for j in range(len(prefix)):
            sortedFreq[prefix[j][1]] = nums[j]
            k = j        
        for i in range(len(sortedFreq)):
            if sortedFreq[i] == None:
                k += 1
                sortedFreq[i] = nums[k]
        runningSum = 0
        for i in range(len(sortedFreq)):
            runningSum += sortedFreq[i]
            sortedFreq[i] = runningSum
        maxSum = 0
        for request in requests:
            maxSum += sortedFreq[request[1]]
            maxSum -= sortedFreq[request[0]-1] if request[0] != 0 else 0
        return maxSum % (10**9 + 7)
