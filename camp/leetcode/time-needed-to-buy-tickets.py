class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque(tickets)
        time_taken = 0
        while queue and queue[k] > 0:
            if queue[0] > 0:
                time_taken += 1
            cur = queue.popleft() - 1
            queue.append(cur)
            if k > 0:
                k -= 1
            else:
                k = len(queue) - 1
        return time_taken

