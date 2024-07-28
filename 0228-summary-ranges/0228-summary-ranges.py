class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return
        prev = nums[0]
        nums.append(float("inf"))
        ans = []
        arror = '->'
        
        for x in range(len(nums)-1):
            if nums[x+1] - 1 != nums[x]:
                if prev == nums[x]:
                    ans.append(str(prev))
                    prev = nums[x+1]
                else:
                    ans.append(str(prev)+arror+str(nums[x]))
                    prev = nums[x+1]
        
        # if prev != nums[-1]:
        #     ans.append(str(prev)+arror+str(nums[-1]))
        # else:
        #     ans.append(str(prev))

        return ans
                
                
        