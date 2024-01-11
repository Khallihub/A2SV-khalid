class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left, right = 0, k
        win = Counter(blocks[:k])
        min_ = win["W"]
        while right < len(blocks):
            win[blocks[right]] += 1
            win[blocks[left]] -= 1
            min_ = min(min_, win["W"])
            right += 1
            left += 1
        return min_