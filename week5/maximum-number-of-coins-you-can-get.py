class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        max_coins = 0
        piles.sort()
        for i in range(len(piles)-2,len(piles)//3-1,-2):
            max_coins += piles[i]
        return max_coins
