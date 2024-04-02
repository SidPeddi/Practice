from heapq import *
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        heap = []
        ans = []
        hashmap = dict( Counter(words))
        for key, value in hashmap.items():
            heappush(heap, (-value, key))
        for x in range(k):
            _, i = heappop(heap)
            ans.append(i)
        return ans
            
        