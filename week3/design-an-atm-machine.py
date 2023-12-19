class ATM:

    def __init__(self):
        self.atm = defaultdict(int)

    def deposit(self, banknotesCount: List[int]) -> None:
        self.atm[500] += banknotesCount[4]
        self.atm[200] += banknotesCount[3]
        self.atm[100] += banknotesCount[2]
        self.atm[50] += banknotesCount[1]
        self.atm[20] += banknotesCount[0]

    def withdraw(self, amount: int) -> List[int]:
        tmp = 0
        res = {20:0, 50:0, 100:0, 200:0, 500:0}
        for k,v in self.atm.items():
            cnt = (amount- tmp) //k
            if cnt >= 1:
                res[k] += min(v,cnt)
                tmp += min(cnt,v) * k
            if tmp >= amount:
                break
        if tmp == amount:
            for k,v in res.items():
                self.atm[k] -= v
            return res.values()
        return [-1]
            


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)