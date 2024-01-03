class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        if len(skill) == 2: return skill[0]*skill[1]
        skill.sort()
        left, right = 1,len(skill)-2
        res = 0
        while left-1 < right+1:
            if skill[left] + skill[right] != skill[left-1] + skill[right+1]:
                return -1
            res += skill[left-1]*skill[right+1]
            left += 1
            right -= 1
        return res

