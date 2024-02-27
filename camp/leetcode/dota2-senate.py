class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        Rs = [i for i in range(len(senate)) if senate[i] == "R"]
        Ds = [i for i in range(len(senate)) if senate[i] == "D"]
        Rs = deque(Rs)
        Ds = deque(Ds)

        banned = set()
        i = 0
        while Rs and Ds:
            if i%len(senate) in banned:
                i += 1
                continue
            if senate[i%len(senate)]  == "D":
                banned.add(Rs.popleft())
                Ds.append(Ds.popleft())
            else:
                banned.add(Ds.popleft())
                Rs.append(Rs.popleft())
            i += 1
        return "Dire" if Ds else "Radiant"
