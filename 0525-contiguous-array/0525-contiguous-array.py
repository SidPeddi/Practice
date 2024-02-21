class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        count = 0
        counts = {}
        counts[0] = -1
        
        
        for i, num in enumerate(nums):
            count += 1 if num else -1
            if count in counts:
                ans = max(ans, i - counts[count] )
            else:
                counts[count] = i
        return ans
            
                