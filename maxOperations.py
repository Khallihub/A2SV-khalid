class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = collections.Counter(nums)
        output = 0
        seen = set()
        for x in count:
            if x not in seen and (k-x) in count:
                if x == (k-x):
                    output += count[x]//2
                else:
                    output += min(count[x], count[k-x])

                seen.add(x)
                seen.add(k-x)
        return output
