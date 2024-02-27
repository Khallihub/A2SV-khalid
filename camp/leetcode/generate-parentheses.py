class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = set()
        def backtrack(cur):
            if len(cur) == 2*n:
                if cur.count("("):
                    ans.add("".join(cur))
                    return

            opened = cur.count("(")
            closed = cur.count(")")
            if closed > opened or opened > n:
                return
            if opened > closed:
                if opened < n:
                    cur.append("(")
                    backtrack(cur)
                    cur.pop()
                cur.append(")")
                backtrack(cur)
                cur.pop()
            elif opened == closed:
                cur.append("(")
                backtrack(cur)
                cur.pop()
        backtrack([])
        return sorted(list(ans))
