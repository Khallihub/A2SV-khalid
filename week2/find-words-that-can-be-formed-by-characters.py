class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_dc = Counter(list(chars))
        res = 0
        for i in range(len(words)):
            cur_dc = Counter(list(words[i]))
            for j in cur_dc:
                if cur_dc[j] > chars_dc[j]:
                    break
            else:
                res += len(words[i])
        return res
        
