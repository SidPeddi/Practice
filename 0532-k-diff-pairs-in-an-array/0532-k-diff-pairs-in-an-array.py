class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = 0
        numset = set(nums)
        counter = Counter(nums)
        if k > 0:
            for x in numset:
                if (x+k) in numset:
                    ans += 1
        else:
            for x in numset:
                if counter[x] > 1:
                    ans += 1
        return ans