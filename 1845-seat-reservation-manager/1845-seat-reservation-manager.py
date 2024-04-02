from heapq import *
class SeatManager:

    def __init__(self, n: int):
        self.heap = []
        for i in range(n):
            heappush(self.heap, i+1)
        

    def reserve(self) -> int:
        return heappop(self.heap)
        
        

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.heap,seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)