class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        result = []
        prefix = 0
        n = len(nums)
        for i in range(n):
            suffix = total - prefix
            right_diff = suffix - ((n - i) * nums[i])
            left_diff = prefix - (i * nums[i])
            abs_diff = abs(right_diff) + abs(left_diff)
            result.append(abs_diff)
            prefix += nums[i]
        return result