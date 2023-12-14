class Solution:
    def minimizedStringLength(self, s: str) -> int:
        cnt = Counter(s)
        reduced = 0
        print(cnt)
        for k,v in cnt.items():
            if v > 2:    
                reduced += v - 1
            elif v == 2:
                reduced += 1
        return len(s) - reduced