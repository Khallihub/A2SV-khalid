class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        idxs = {}
        for i in range(len(candidates)):
            cur = idxs.get(candidates[i],-1) 
            if cur == -1:
                idxs[candidates[i]] = i
        idxs = idxs.values()
        ans = set()
        cnt = Counter(candidates)
        if sum(candidates) < target:
            return []
        def backtrack(used,total):
            tmp = 0
            nums = []
            if total == target:
                for i,v in used.items():
                    tmp += i*v
                    for j in range(v):
                        nums.append(i)
                ans.add(tuple(sorted(nums)))
                return
            if total > target:
                return

        
            for i in idxs:
                if cnt[candidates[i]] == used[candidates[i]]:
                    continue
                used[candidates[i]] += 1
                total += candidates[i]
                backtrack(used,total)
                used[candidates[i]] -= 1
                total -= candidates[i]
                if used[candidates[i]] == 0:
                    del used[candidates[i]]
        backtrack(defaultdict(int),0)
        return ans