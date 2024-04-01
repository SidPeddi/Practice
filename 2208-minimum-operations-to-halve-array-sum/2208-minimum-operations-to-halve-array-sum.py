import heapq

class Solution:
    def halveArray(self, nums: List[int]) -> int:
        total = sum(nums)/2
        nums = [-num for num in nums]
        heapq.heapify(nums) # turns an array into a heap in linear time
        count = 0
        while (total) > 0:
            first = (heapq.heappop(nums)/2)
            heapq.heappush(nums, (first))
            total += first
            count += 1
        return count