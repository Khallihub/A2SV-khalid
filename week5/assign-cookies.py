class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        t,b = 0,0
        content = 0
        while t < len(g) and b < len(s):
            if g[t] <= s[b]:
                content += 1
                t += 1
                b += 1
            while t < len(g) and b < len(s) and g[t] > s[b]:
                b += 1
        return content