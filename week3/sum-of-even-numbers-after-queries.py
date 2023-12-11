class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        answer = []
        total = 0
        for i in range(len(nums)):
            if nums[i]%2 == 0:
                total += nums[i]
        for i in range (len(queries)):
            tmp = nums[queries[i][1]]
            nums[queries[i][1]] += queries[i][0]
            if tmp%2 == 0 and nums[queries[i][1]] %2 != 0:
                total -= tmp
            elif tmp%2 == 0 and nums[queries[i][1]] %2 == 0:
                total += queries[i][0]
            elif tmp%2 != 0 and nums[queries[i][1]] %2 == 0:
                total += nums[queries[i][1]]
            answer.append(total)
        return answer