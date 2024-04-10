class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for x in nums:
            if not x:
                nums.remove(x)
                nums.append(x)
        
        