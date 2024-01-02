class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort(reverse=True)
        processorTime.sort()
        min_time = 0
        for i in range(len(processorTime)):
            for j in range(i*4,i*4+4):
                min_time = max(min_time, processorTime[i]+tasks[j])
        return min_time
