class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        answer = []
        for i in range (len(l)):
            flag = True
            sub = nums[l[i]:r[i]+1]
            sub.sort()
            diff = sub[1] - sub[0]
            for i in range (len(sub)-1):
                if sub[i] + diff != sub[i+1]:
                    answer.append(False)
                    flag = False
                    break
            if flag == True:
                answer.append(True)
        return answer
