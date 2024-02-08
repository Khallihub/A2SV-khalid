class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""
        t_cnt = Counter(t)
        win = defaultdict(int)
        for i in range(len(t)):
            win[s[i]] += 1

        def check(a,b):
            for i,v in b.items():
                if a[i] < v:
                    return False
            else:
                return True
        min_ = [0, len(s)+2]
        left,right = 0,len(t)
        while right <= len(s):
            while check(win, t_cnt):
                min_ = [left,right] if right-left <= min_[1]-min_[0] else min_
                win[s[left]] -= 1
                left += 1
            if right < len(s):
                win[s[right]] += 1
            right += 1
        if min_[1] == len(s)+2:
            return ""
        return s[min_[0]:min_[1]]