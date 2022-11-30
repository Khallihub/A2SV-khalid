class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        answer = 0 
        i = len(piles)/3
        k = len(piles)
        while i > 0:
            answer += piles[k-2]
            i-=1
            k-=2
        return answer
