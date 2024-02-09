class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        totalSeats = [0 for i in range(n)]
        for booking in bookings:
            totalSeats[booking[0]-1] += booking[2]
            if booking[1] + 1 <= n:
                totalSeats[booking[1]] -= booking[2]
        runningSum = 0
        for i in range(len(totalSeats)):
            runningSum += totalSeats[i]
            totalSeats[i] = runningSum
        return totalSeats