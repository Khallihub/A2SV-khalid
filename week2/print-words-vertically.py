class Solution:
    def printVertically(self, s: str) -> List[str]:
        res = []
        words = s.split(" ")
        max_len = 0
        for k in words:
            max_len = max(max_len, len(k))
        for i in range(max_len):
            cur = ""
            print(res)
            for j in range(len(words)):
                if len(words[j]) > i:
                    cur += words[j][i]
                else:
                    cur += " "
            res.append(cur.rstrip())
        return res
        
"""
CONTEST 
IS 
COMING
"""