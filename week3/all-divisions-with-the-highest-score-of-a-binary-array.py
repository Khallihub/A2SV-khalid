class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        zeros = [0]
        ones = [0]
        zeroCnt = 0
        oneCnt = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeroCnt += 1
            zeros.append(zeroCnt)
            if nums[len(nums)-1-i] == 1:
                oneCnt += 1
            ones.append(oneCnt)
        ones.reverse()
        max_ = float("-inf")
        for i in range(len(zeros)):
            zeros[i] = zeros[i] + ones[i]
            max_ = max(max_, zeros[i])
        res = []
        for i in range(len(zeros)):
            if zeros[i] == max_:
                res.append(i)
        return res
        
        