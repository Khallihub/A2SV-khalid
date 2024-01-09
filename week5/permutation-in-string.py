class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        win = Counter(s2[:len(s1)])
        left, right = 0, len(s1)
        s1 = Counter(s1)
        while right <= len(s2):
            print(win)
            if win == s1:
                return True
            if right < len(s2):
                if s2[right] in win:
                    win[s2[right]] += 1
                else:
                    win[s2[right]] = 1
                win[s2[left]] -= 1
                if win[s2[left]] == 0:
                    del win[s2[left]]
            left += 1
            right +=1
        return False
