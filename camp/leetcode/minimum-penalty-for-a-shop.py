class Solution:
    def bestClosingTime(self, customers: str) -> int:
        openPen = 0
        closePen = 0
        for i in range(len(customers)):
            closePen += 1 if customers[i] == "Y" else 0
        min_pen = len(customers) + 1
        min_hour = 0
        print(openPen, closePen)
        for i in range(len(customers)):
            penalty = openPen + closePen
            min_hour = i if penalty < min_pen else min_hour
            min_pen = min(min_pen, penalty)
            if customers[i] == "Y":
                closePen -= 1
            else:
                openPen += 1
        penalty = openPen + closePen
        min_hour = i if penalty < min_pen else min_hour
        if min_hour == len(customers) - 1 and customers[-1] == "Y":
            min_hour += 1
        return min_hour