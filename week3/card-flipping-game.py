class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        f = defaultdict(list)
        b = defaultdict(list)
        for i in range(len(fronts)):
            f[fronts[i]].append(i)
            b[backs[i]].append(i)
        min_ = tmp = max([*fronts, *backs]) + 1 
        for i in backs:
            if not i in f:
                min_ = min(min_, i)
        for i,v in enumerate(fronts):
            fidx = set(f[v])
            bidx = set(b[v])
            if not fidx & bidx:
                min_ = min(v, min_)
        if min_ == tmp:
            return 0
        return min_


