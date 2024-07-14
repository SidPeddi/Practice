class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        hashset = set()
        ans = 0
        l = 0
        tsum = 0
        for x in range(len(nums)):
            while nums[x] in hashset:
                hashset.remove(nums[l])
                tsum -= nums[l]
                l += 1
            hashset.add(nums[x])
            tsum += nums[x]
            ans = max(tsum,ans)
        return ans
                
            
            
            
        