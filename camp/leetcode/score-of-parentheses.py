class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stk = []
        score = 0
        for i in s:
            if i == "(":
                stk.append(score)
                score = 0
            else:
                score = stk.pop() + max(score*2, 1)
            print(stk, score)
        return score