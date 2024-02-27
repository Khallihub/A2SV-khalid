class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        powerSet = set()

        def backtrack(cur, index):
            if len(cur) <= len(nums):
                tmp = tuple(sorted(cur))
                if not tmp in powerSet:
                    powerSet.add(tmp[:])


            for i in range(index, len(nums)):
                if nums[i] in cur:
                    continue
                cur.append(nums[i])
                backtrack(cur, index+1)
                cur.pop()

        backtrack([],0)
        return powerSet
