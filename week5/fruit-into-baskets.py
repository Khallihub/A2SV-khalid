class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        unique = defaultdict(int)
        left,right,res = 0,0,0
        cur = 0
        while right < len(fruits):
            unique[fruits[right]] += 1
            while len(unique) > 2:
                cur -= 1
                unique[fruits[left]] -=1
                if unique[fruits[left]] == 0:
                    del unique[fruits[left]]
                left += 1
            cur += 1
            res = max(cur, res)
            right += 1
        return res