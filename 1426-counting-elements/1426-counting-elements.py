class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        map = set(arr)
        counter = 0
        for i in arr:
            if ((i)+1) in map:
                counter += 1
        return counter
        