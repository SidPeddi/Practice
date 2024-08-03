class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        ans = 0
        for x in nums:
            if (x-1) not in nums:
                length = 1
                while x + length in nums:
                    length += 1
                ans = max(ans,length)
            
        return ans
                
        