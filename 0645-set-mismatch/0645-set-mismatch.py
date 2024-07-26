class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = ((len(nums)+1)*(len(nums)))//2
        return [sum(nums)-sum(set(nums)),ans-sum(set(nums))]
      