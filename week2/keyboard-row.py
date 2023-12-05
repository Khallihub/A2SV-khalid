class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        fr = Counter("qwertyuiop")
        sr = Counter("asdfghjkl")
        tr = Counter("zxcvbnm")
        res = []
        for i in words:
            if i[0].lower() in fr:
                for j in i:
                    if j.lower() not in fr:
                        break
                else:
                    res.append(i)
            elif i[0].lower() in sr:
                for j in i:
                    if j.lower() not in sr:
                        break
                else:
                    res.append(i)
            elif i[0].lower() in tr:
                for j in i:
                    if j.lower() not in tr:
                        break
                else:
                    res.append(i)
        return res