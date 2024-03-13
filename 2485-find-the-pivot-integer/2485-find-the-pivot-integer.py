class Solution:
    def pivotInteger(self, n: int) -> int:
        if n == 1:
            return n
        my_array = [i for i in range(1, n+1)]
        for i in range(1, n+1):
            if sum(my_array[:i+1]) == sum(my_array[i:]):
                return i+1
        return -1
            