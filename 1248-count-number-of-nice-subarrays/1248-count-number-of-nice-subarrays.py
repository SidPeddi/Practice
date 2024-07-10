class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = []
        m = 0
        sums = 0
        count = 0
        l = 0
        for x in nums:
            ans.append(x % 2)
        
        for r in ans:
            sums += r
            
            while sums > k:
                sums -= ans[l]
                l += 1
                m = l
                
            if sums == k:
                while ans[m] == 0:
                    m += 1
                count += (m-l) + 1
            print(r,sums)
        return count
            
        