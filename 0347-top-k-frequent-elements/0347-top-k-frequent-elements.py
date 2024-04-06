class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        items = Counter(nums).items()
        heap = []
        ans = []
        for key,v in items:
            heapq.heappush(heap, (-v,key))
        while k > 0:
            _,key = heapq.heappop(heap)
            ans.append(key)
            k -= 1
        return ans
        