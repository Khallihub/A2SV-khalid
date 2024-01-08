class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        t_cnt, f_cnt, left, right= 0,0,0,0
        confusion = 0
        while right < len(answerKey):
            if answerKey[right] == "T": t_cnt += 1
            else: f_cnt += 1
            while t_cnt > k and f_cnt > k:
                if answerKey[left] == "T": t_cnt -= 1
                else: f_cnt -= 1
                left += 1
            confusion = max(confusion,t_cnt+f_cnt)
            right += 1
        return confusion
            
        