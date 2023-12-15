class Bitset:

    def __init__(self, size: int):
        self.size = size
        self.bitset = ["0"]*size
        self.flipped = False
        self.Onescount = 0
        

    def fix(self, idx: int) -> None:
        if self.flipped:
            if self.bitset[idx] != "0":
                self.Onescount += 1
            self.bitset[idx] = "0"
        else:
            if self.bitset[idx] != "1":
                self.Onescount += 1
            self.bitset[idx] = "1"

    def unfix(self, idx: int) -> None:
        if self.flipped:
            if self.bitset[idx] != "1":
                self.Onescount -= 1
            self.bitset[idx] = "1"   
        else:
            if self.bitset[idx] != "0":
                self.Onescount -= 1
            self.bitset[idx] = "0"
        
    def flip(self) -> None:
        self.flipped = not self.flipped
        self.Onescount = self.size - self.Onescount

    def all(self) -> bool:
        return self.size == self.Onescount      

    def one(self) -> bool:
        return self.Onescount > 0      

    def count(self) -> int:
        return self.Onescount        

    def toString(self) -> str:
        if self.flipped:
            tmp = ["1" if i == "0" else "0" for i in self.bitset]
            return "".join(tmp)
        else:
            return "".join(self.bitset)
        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()