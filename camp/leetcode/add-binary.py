class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        carry = 0

        a = deque(a)
        b = deque(b)

        diff = abs(len(a) - len(b))       

        if len(a) > len(b):
            while diff:
                b.appendleft("0")
                diff -= 1
        else:
            while diff:
                a.appendleft("0")     
                diff -= 1
        
        for i in range(len(a)-1, -1, -1):
            s = int(a[i])+ int(b[i]) + carry
            carry = 0

            if s == 0: res.append(str(s))
            elif s == 1: res.append(str(s))
            elif s == 2:
                res.append(str(0))
                carry = 1
            elif s == 3:
                res.append(str(1))
                carry = 1
        if carry: res.append("1")
        res.reverse()
        return "".join(res)