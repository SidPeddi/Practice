import heapq


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-pile for pile in piles]
        heapq.heapify(piles)
        for i in range (k):
            first = abs(heapq.heappop(piles))
            first -= (first//2)
            heapq.heappush(piles, -abs(first))
        return -sum(piles)