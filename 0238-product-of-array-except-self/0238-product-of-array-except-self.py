class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prev = [1]*len(nums)
        post = [1]*len(nums)
        for i in range(1,len(nums)):
            prev[i] *= prev[i-1] * nums[i -1]
        nums.reverse()
        for i in range(1,len(nums)):
            post[i] *= post[i-1] * nums[i -1]
        post.reverse()
        for i in range(len(nums)):
            prev[i] *= post[i] 
        return prev