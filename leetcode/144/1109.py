class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        r = [0]*n
        for a in bookings:
            r[a[0]-1] += a[2]
            if a[1] < n:
                r[a[1]] -= a[2]
        for i in range(1,n):
            r[i] += r[i-1]
        return r