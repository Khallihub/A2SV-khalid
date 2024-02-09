class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        total_shifts = [0 for i in range(len(s))]
        for shift in shifts:
            total_shifts[shift[0]] += 1 if shift[2] == 1 else -1
            if shift[1] < len(s)-1:
                total_shifts[shift[1]+1] -= 1 if shift[2] == 1 else -1
        runningSum = 0
        for i in range(len(total_shifts)):
            runningSum += total_shifts[i]
            total_shifts[i] = runningSum
        ords = [ord(i) for i in s]
        for i in range(len(ords)):
            total_shifts[i] = total_shifts[i]%26 if total_shifts[i] >= 0 else total_shifts[i]%-26
            if ords[i] + total_shifts[i] > 122:
                ords[i] = chr(96 + ords[i] + total_shifts[i] - 122)
            elif  ords[i] + total_shifts[i] < 97:
                ords[i] = chr(123 + (ords[i] - abs(total_shifts[i]) - 97))
            else:
                ords[i] = chr(ords[i] + total_shifts[i])
        return "".join(ords)
