class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        seq = {}
        for i, v in enumerate(order):
            seq[v] = i 
        print(seq)
        for i in range (len(words)-1):
            j = 0
            rg = min(len(words[i]), len(words[i+1]))
            while j < rg:
                print(words[i][j],words[i+1][j])
                if seq[words[i][j]] < seq[words[i+1][j]]:
                    break
                if seq[words[i][j]] > seq[words[i+1][j]]:
                    return False
                j += 1
            else:
                if len(words[i]) > len(words[i + 1]):
                    return False

        return True

