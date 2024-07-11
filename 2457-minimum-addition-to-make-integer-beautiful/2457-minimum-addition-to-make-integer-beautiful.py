class Solution(object):
    def makeIntegerBeautiful(self, n, target):
        """
        :type n: int
        :type target: int
        :rtype: int
        """
        nth = len(str(n))
        ans = n
        nsum = 0
        for i in str(n):
            nsum += int(i)
        if nsum <= target:
                return n - ans
        for x in range(1,nth+1):
            count = (10 ** x) - (n % (10 ** x))
            n += count
            nsum = 0
            for i in str(n):
                nsum += int(i)
            if nsum <= target:
                return n - ans
            
                
        return n - ans
            