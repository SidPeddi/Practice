class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashset = set()
        notset = set()
        for x in nums:
            if x in hashset and x not in notset:
                hashset.remove(x)
                notset.add(x)
            if x not in notset:
                hashset.add(x)
        return sum(hashset)
        