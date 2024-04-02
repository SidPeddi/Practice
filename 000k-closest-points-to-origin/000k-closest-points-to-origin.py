class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        ans = []
        for i in points:
            count = ((i[0] ** 2) + (i[1] ** 2))
            heappush(heap, (count, i[0],i[1]))
        for x in range(k):
            _,l,r= heappop(heap)
            ans.append([l,r])
        return ans