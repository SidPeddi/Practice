class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = ((n+1)*(n))//2
        numset = set(nums)
        return [sum(nums)-sum(numset),ans-sum(numset)]
      