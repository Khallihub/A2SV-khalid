class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        operations = []
        for i in range(len(boxes)):
            cur = 0
            for j,v in enumerate(boxes):
                if j == i:
                    continue
                if v == "1":
                    cur += abs(i-j)
            operations.append(cur)
        return operations
                