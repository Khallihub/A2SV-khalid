class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backtrack(candidate, last):
            # handle basecases
            if len(candidate) == k:
                ans.append(candidate[:])
                return
            # iterate all possible candidates.
            for next_candidate in range(last+1, n+1):
                    candidate.append(next_candidate)
                    # given the candidate, explore further.
                    backtrack(candidate,next_candidate)
                    # backtrack
                    candidate.pop()
        backtrack([],0)
        return ans
