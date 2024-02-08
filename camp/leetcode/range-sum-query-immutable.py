class NumArray:

    def __init__(self, nums: List[int]):
        self.runningSum = 0
        self.nums = nums
        self.prefix = []
        for i in nums:
            self.runningSum += i
            self.prefix.append(self.runningSum)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right] - self.prefix[left] + self.nums[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)