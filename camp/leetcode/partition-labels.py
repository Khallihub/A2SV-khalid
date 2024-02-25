class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = defaultdict(int)
        for i,v in enumerate(s):
            lastIndex[v] = i
        res = []
        i = 0
        while i < len(s):
            start = i
            end = lastIndex[s[i]]
            while i < end:
                end = max(end, lastIndex[s[i]])
                i += 1
            res.append(end-start+1)
            i += 1
        return res