class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums
        if 2*k > len(nums)+1:
            return [-1] * len(nums)
        prefix = [0, nums[0]]
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])      
        
        res = [-1] * k
        l = 2*k+1
        for x in range(k+1,len(prefix)-k):
            res.append((prefix[x+k] - prefix[x-k-1])//l)
        return res + [-1] * k
                
            