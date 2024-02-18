class Solution:
    def simplifyPath(self, path: str) -> str:
        stk = path.split("/")
        res = []
        for i in range(len(stk)):
            if stk[i] == "..":
                if len(res) > 0:    
                    res.pop()
            else:
                if stk[i] != "" and stk[i] != ".":
                    res.append(stk[i])
        return "/" + "/".join(res)