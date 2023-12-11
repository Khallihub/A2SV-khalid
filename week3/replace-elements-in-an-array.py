class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        cnt = Counter(nums)
        idxs = {}
        for i,v in enumerate(nums):
            idxs[v] = i
        for i in range(len(operations)):
            nums[idxs[operations[i][0]]] = operations[i][1]
            idxs[operations[i][1]] = idxs[operations[i][0]]
        return nums