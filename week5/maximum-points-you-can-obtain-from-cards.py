class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        points = sum(cardPoints[:k])
        cur = points
        left, right = k-1, len(cardPoints)-1
        while left >= 0:
            cur -= cardPoints[left]
            cur += cardPoints[right]
            points = max(points, cur)
            left -= 1
            right -= 1
        return points