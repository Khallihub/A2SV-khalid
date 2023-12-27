class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        cnt = 0
        max_ = flips[0]
        for i in range(len(flips)):
            max_ = max(max_, flips[i])
            print(max_,i+1,flips[i])
            if max_ == i+1:
                cnt += 1
        return cnt