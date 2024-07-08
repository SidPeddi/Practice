class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        myset = set(nums)
        length = 0
        ans = 0
        for x in myset:
            if (x-1) not in myset:
                while (x + length) in myset:
                    length += 1
                ans = max(ans,length)
                length = 0
        return ans
                
        