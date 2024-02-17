class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        total = 0
        cnt = defaultdict(int)
        for rabbit in answers:
            if cnt[rabbit] <= 0:
                total += rabbit +1
                cnt[rabbit] += rabbit
            else:
                cnt[rabbit] -= 1
        return total