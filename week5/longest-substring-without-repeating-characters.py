class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ht = Counter()
        max_ = left = 0
        for i in range(len(s)):
            while s[i] in ht:
                ht[s[left]] -= 1
                if ht[left] == 0:
                    ht.pop(s[left])
                left += 1
            max_ = max(max_, i - left + 1)
            ht[s[i]] += 1

        return max_  