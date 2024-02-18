class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack1 = []
        for i in range (len(tokens)):
            if tokens[i] != "+" and  tokens[i] != "-" and tokens[i] != "*" and tokens[i] != "/":
                stack1.append(int(tokens[i]))
            else:
                a = stack1.pop()
                b = stack1.pop()
                exp = f"{b} {tokens[i]} {a}" 
                c = eval(exp) if tokens[i] != "/" else math.trunc(b/a)
                stack1.append(c)
        return stack1[0]