class Solution:
    def decodeHelper(self, s: str) -> list:
        i = 0
        while s[i].isdigit():
            i += 1
        if i:
            reps = int(s[:i])
            j = i
            stk = [s[i]]
            for k in range(i+1,len(s)):
                j += 1
                if stk and s[k] == "]":
                    stk.pop()
                if len(stk) == 0:
                    break
                if s[k] == "[":
                    stk.append(s[k])
            chars = s[i+1:j]
            j += 1
        else:
            reps = 1
            j = 0
            while j < len(s) and s[j].isalpha():
                j += 1
            chars = s[:j]
        return [chars, reps, j]
    def decodeString(self, s: str) -> str:
        if len(s) < 1:
            return ""
        if s.isalpha():
            return s
        chars, reps, j = self.decodeHelper(s)
        return self.decodeString(chars) * reps + self.decodeString(s[j:])
        