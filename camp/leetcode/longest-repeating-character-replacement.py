class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left,right = 0,0
        win = defaultdict(int)
        max_ = 0
        while right < len(s):
            win[s[right]] += 1
            while sum(win.values()) - max(win.values()) > k:
                win[s[left]] -= 1
                left += 1
            max_ = max(max_,right-left+1)
            right += 1
        return max_