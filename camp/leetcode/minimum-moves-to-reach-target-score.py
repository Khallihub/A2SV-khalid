class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        moves = 0
        halfed = 0
        decremented = 0 if target%2 == 0 else 1
        tmp = target if target%2 == 0 else target-1
        while maxDoubles > 0 and tmp >= 1:
            tmp /= 2
            halfed += 1
            if tmp % 2 != 0:
                tmp -= 1
                decremented += 1
            maxDoubles -= 1
        decremented += tmp-1
        return int(decremented + halfed)