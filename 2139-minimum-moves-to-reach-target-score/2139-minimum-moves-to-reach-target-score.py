class Solution(object):
    def minMoves(self, target, maxDoubles):
        """
        :type target: int
        :type maxDoubles: int
        :rtype: int
        """
        count = 0
        while target > 1:
            if target % 2 and maxDoubles > 0:
                target -= 1
                count += 1
            elif target % 2 == 0 and maxDoubles > 0:
                target //= 2
                count += 1
                maxDoubles -= 1
            else:
                count += target - 1
                target = 1
        return count