class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loss = {}
        win = set()
        for i  in range(len(matches)):
            loss[matches[i][1]] = loss.get(matches[i][1], 0) + 1
            win.add(matches[i][0])
        print(loss, win)
        res = [[],[]]
        for k,v in loss.items():
            if v == 1:
                res[1].append(k)
        for i in win:
            if not i in loss:
                res[0].append(i)
        res[0].sort()
        res[1].sort()
        return res