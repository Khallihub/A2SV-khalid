class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        monoStk = []
        min_ = float("inf")
        for i in range(len(nums)):
            while monoStk and monoStk[-1][0] <= nums[i]:
                top = monoStk.pop()
            if monoStk and nums[i] < monoStk[-1][0] and nums[i] > monoStk[-1][1]:
                return True
            monoStk.append([nums[i], min_])
            min_ = min(min_, nums[i])
        return False