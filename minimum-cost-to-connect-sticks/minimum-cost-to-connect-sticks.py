import heapq

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        count = 0
        while len(sticks) > 1:
            first = (heapq.heappop(sticks))
            second = (heapq.heappop(sticks))
            heapq.heappush(sticks, first + second)
            count += second + first
        return count

