class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = 0
        myset = set(nums)

        if k == 0:
            maps = {}
            for x in nums:
                maps[x] = maps.get(x,0) + 1
            for x in myset:
                if maps[x] > 1:
                    ans += 1
        else:
            for x in myset:
                if (x-k) in myset:
                    ans += 1
        return ans