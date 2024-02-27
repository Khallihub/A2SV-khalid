class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        powerSet = set()
        cnt = Counter(nums)

        def backtrack(cur, index):
            nonlocal cnt
            for i in cur:
                if cur[i] > cnt[i]:
                    return
            tmp = []
            for i in cur:
                for j in range(cur[i]):
                    tmp.append(i)
            tmp = tuple(sorted(tmp))
            if not tmp in powerSet:
                powerSet.add(tmp[:])


            for i in range(index, len(nums)):
                cur[nums[i]] += 1
                backtrack(cur, index+1)
                cur[nums[i]] -= 1
                if cur[nums[i]] == 0:
                    del cur[nums[i]]
        cur = defaultdict(int)
        backtrack(cur,0)
        return sorted(powerSet)