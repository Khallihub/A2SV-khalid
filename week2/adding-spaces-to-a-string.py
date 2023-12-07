class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = ""
        words = []
        start = 0
        i = 0
        while i < len(spaces):
            end = spaces[i]
            words.append(s[start:end])
            start = end
            i += 1
        words.append(s[end:])
        return " ".join(words)