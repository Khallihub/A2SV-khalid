class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack1 = []
        for i in s:
            if i != ")":
                stack1.append(i)
            else:
                a = ""
                while len(stack1)>0 and stack1[-1] != "(":
                    if len(stack1[-1]) > 1:
                        c = stack1.pop()
                        c = c[::-1]
                        a += c
                    else:
                        b = stack1.pop()
                        a += b
                stack1.pop()
                stack1.append(a)
        ans = "".join(stack1)
        return ans 
