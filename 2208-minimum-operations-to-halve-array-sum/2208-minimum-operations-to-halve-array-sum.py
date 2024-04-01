import heapq

class Solution:
    def halveArray(self, nums: List[int]) -> int:
        tot = total = sum(nums)
        nums = [-num for num in nums]
        heapq.heapify(nums) # turns an array into a heap in linear time
        count = 0
        while (tot/2) < total:
            first = (heapq.heappop(nums)/2)
            heapq.heappush(nums, (first))
            total += first
            count += 1
            print(first)
            print(total)
            print(count)
        return count