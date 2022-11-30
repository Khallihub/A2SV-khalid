class Solution:
    def isValid(self, s: str) -> bool:
        lst = []
        for i in s:
            if i == "(" or i == "{" or i == "[":
                lst.append(i)
            elif i == ")":
                if len(lst) == 0:
                    return False
                elif lst[-1] == "(":
                    lst.pop()
                else:
                    return False
            elif i == "}":
                if len(lst) == 0:
                    return False
                elif lst[-1] == "{":
                    lst.pop()
                else:
                    return False 
            elif i == "]":
                if len(lst) == 0:
                    return False
                elif lst[-1] == "[":
                    lst.pop()
                else:
                    return False
        if len(lst) != 0:
            return False
        else:
            return True
