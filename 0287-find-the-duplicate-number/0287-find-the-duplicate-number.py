class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashset = set()
        for x in nums:
            if x in hashset:
                return x
            hashset.add(x)