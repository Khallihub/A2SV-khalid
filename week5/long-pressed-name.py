class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        first, second = 0,0
        while second < len(typed):
            if first < len(name) and name[first] == typed[second]:
                first += 1 
            elif second == 0 or typed[second] != typed[second-1]:
                return False
            second += 1
        return first == len(name)

