class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        monotonic_stack = []
        total = 0
        for i in range(len(arr)+1):
            while i == len(arr) or (monotonic_stack and arr[i] < monotonic_stack[-1][0]):
                top = monotonic_stack.pop()
                right = i - top[1]
                left = 1
                if monotonic_stack:
                    left = top[1] - monotonic_stack[-1][1]
                else:
                    left = top[1] + 1
                tmp = right * left if left else right
                total += top[0] * tmp
                if i == len(arr) and not monotonic_stack:
                    break
            if i < len(arr):               
                monotonic_stack.append([arr[i], i])
        return total % (10**9 + 7)