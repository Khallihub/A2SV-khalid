class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stk = []
        closed = 0
        for i in s:
            if stk and i == ")":
                stk.pop()
            elif not stk and i == ")":
                closed += 1
            if i == "(":
                stk.append(i)
        return len(stk) + closed