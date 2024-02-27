class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()

        def backtrack(cur):
            if sum(cur) == target:
                tmp = tuple(sorted(cur))
                if not tmp in res:
                    res.add(tmp)
                return
            if sum(cur) > target:
                return

            for i in range(len(candidates)):
                cur.append(candidates[i])
                backtrack(cur)
                cur.pop()
        backtrack([])
        return res