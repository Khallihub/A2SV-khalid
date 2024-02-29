class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = set()
        def backtrack(used):
            if len(used) == k:
                if sum(used) == n:
                    ans.add(tuple(sorted(used)))
                return
            
            for i in range(1,10):
                if i in used:
                    continue
                used.add(i)
                backtrack(used)
                used.remove(i)
        backtrack(set())
        return ans