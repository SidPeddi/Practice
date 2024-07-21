class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) * len(matrix[0]) - 1
        n = len(matrix[0])
        while left <= right:
            mid = (left + right) // 2
            one = mid // n
            two = mid % n
            if matrix[one][two] == target:
                return True
            if matrix[one][two] > target:
                right = mid - 1 
            else:
                left = mid + 1
        return False