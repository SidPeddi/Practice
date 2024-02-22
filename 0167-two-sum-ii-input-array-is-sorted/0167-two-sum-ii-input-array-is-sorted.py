class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0 
        right = len(numbers) - 1
        total = 0
        while left < right:
            total = target - numbers[left]
            if total < numbers[right]:
                right -= 1
            elif total > numbers[right]:
                left += 1
            else:  
                return [left+1, right+1]

        