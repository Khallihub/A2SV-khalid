class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack1 = []
        for i in range (len(tokens)):
            if tokens[i] != "+" and  tokens[i] != "-" and tokens[i] != "*" and tokens[i] != "/":
                stack1.append(int(tokens[i]))
            else:
                if tokens[i] == "+":
                    a = stack1.pop()
                    b = stack1.pop()
                    c = a + b
                    stack1.append(c)
                elif tokens[i] == "-":
                    a = stack1.pop()
                    b = stack1.pop()
                    c = b - a
                    stack1.append(c)
                elif tokens[i] == "*":
                    a = stack1.pop()
                    b = stack1.pop()
                    c = a * b
                    stack1.append(c)
                elif tokens[i] == "/":
                    a = stack1.pop()
                    b = stack1.pop()
                    stack1.append(math.trunc(b/a))
        return stack1[0]
