class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        brackets = {
            "(" : ")",
            "[" : "]",
            "{" : "}"
        }
        for i in s:
            if i in brackets:
                stk.append(i)
            else:
                if not stk and not i in brackets:
                    return False
                if i != brackets[stk[-1]]:
                    return False
                else:
                    stk.pop()
        return len(stk) == 0
