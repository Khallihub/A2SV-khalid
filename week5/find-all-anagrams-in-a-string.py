class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left, right = 0, len(p)-1
        pwin = Counter(p)
        win = Counter(s[:right+1])
        anagrams = []
        while right < len(s):
            if pwin == win:
                anagrams.append(left)
            if win[s[left]]:
                win[s[left]] -= 1
                if win[s[left]] == 0:
                    del win[s[left]]
            left += 1
            right += 1
            if right < len(s):
                if win[s[right]]:
                    win[s[right]] += 1
                else:
                    win[s[right]] = 1
        return anagrams
        
