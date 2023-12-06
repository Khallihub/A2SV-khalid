class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        idxs = []
        res = []
        for i,value1 in enumerate(list1):
            for j,value2 in enumerate(list2):
                if value1 == value2:
                    idxs.append([i,i+j])
        min_ = 2000
        for i in range(len(idxs)):
            min_ = min(min_,idxs[i][1])
        for i in idxs:
            if i[1] == min_:
                res.append(list1[i[0]])
        return res
