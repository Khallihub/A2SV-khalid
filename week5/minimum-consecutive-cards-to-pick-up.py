class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        unique = set()
        cons = len(cards)+1
        left, right = 0,0
        while right < len(cards):
            while cards[right] in unique:
                cons = min(cons, right-left+1)
                unique.remove(cards[left])
                left +=1
            unique.add(cards[right])
            right += 1
        if cons == len(cards) + 1:
            return -1
        return cons

