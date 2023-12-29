class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        arr = [None]*10
        for word in words:
            temp = word[-1]
            arr[int(temp)] = word[:-1]
        words = []
        res = ""
        for word in arr:
            if word:
                res += word 
                res += " "
        return res[:-1]