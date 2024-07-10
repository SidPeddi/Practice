class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        m = 0
        sums = 0
        count = 0
        l = 0

        for r in nums:
            sums += (r % 2)
            
            while sums > k:
                sums -= (nums[l] % 2)
                l += 1
                m = l
                
            if sums == k:
                while (nums[m] % 2) == 0:
                    m += 1
                count += (m-l) + 1
        return count
            
        