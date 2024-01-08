class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left = right = v_cnt = max_cnt = 0
        N = len(s)
        while right < N:
            if s[right] == "a" or s[right] == "e" or s[right] == "i" or s[right] == "o" or s[right] == "u":
                v_cnt += 1
            if right - left == k:
                if s[left] == "a" or s[left] == "e" or s[left] == "i" or s[left] == "o" or s[left] == "u":
                    v_cnt -= 1
                left += 1
            right += 1
            max_cnt = max(max_cnt, v_cnt)
        return max_cnt
            