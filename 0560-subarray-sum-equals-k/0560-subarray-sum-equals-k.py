class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        
        sum = 0
        count = 0
        dic = {}
        dic[0] = 1
        for x in nums:
            sum += x
            if (sum - k) in dic:
                count += dic[sum - k]
            dic[sum] = dic.get(sum, 0)+1
        return count
        