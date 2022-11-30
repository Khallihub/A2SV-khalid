class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        c = list(count.items())
        c.sort(key= lambda x:x[1],reverse=True)
        print(c)
        answer = []
        for i in range (k):
            answer.append(c[i][0])
        return answer
