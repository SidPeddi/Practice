class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        count = 0
        nums.sort()
        if k != 0:
            nums = set(nums)
            for x in nums:
                if x + k in nums:
                    count += 1
        else:
            counts = Counter(nums)
            for x in list(counts):
                if counts[x] > 1:
                    count += 1
          
        return count
                
            
        
        