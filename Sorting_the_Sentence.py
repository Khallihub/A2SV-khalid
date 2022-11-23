class Solution:
    def sortSentence(self, s: str) -> str:
        a = s.split()
        lst = [None]*9
        for i in a:
            if i[-1] == "1":
                lst[0] = i
            elif i[-1] == "2":
                lst[1] = i
            elif i[-1] == "3":
                lst[2] = i
            elif i[-1] == "4":
                lst[3] = i
            elif i[-1] == "5":
                lst[4] = i
            elif i[-1] == "6":
                lst[5] = i
            elif i[-1] == "7":
                lst[6] = i
            elif i[-1] == "8":
                lst[7] = i
            elif i[-1] == "9":
                lst[8] = i
        try:
            while lst.index(None) != -1:
                if None in lst:
                    lst.remove(None)
        except:
            aa = lst
        s= ""
        for i in aa:
            s+=i[:-1]
            s+=" "
        return s.strip()       
