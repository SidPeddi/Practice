import heapq


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-pile for pile in piles]
        heapq.heapify(piles)
        while k != 0:
            k -= 1
            first = abs(heapq.heappop(piles))
            first -= (first//2)
            heapq.heappush(piles, -abs(first))
        return -sum(piles)