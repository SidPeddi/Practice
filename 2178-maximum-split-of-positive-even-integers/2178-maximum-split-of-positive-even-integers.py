class Solution(object):
    def maximumEvenSplit(self, finalSum):
        """
        :type finalSum: int
        :rtype: List[int]
        """
        if finalSum % 2:
            return []
        numsset = set()
        i = 2
        while finalSum:
            if i not in numsset and (finalSum - i) not in numsset and (finalSum - i) != i:
                numsset.add(i)
                finalSum -= i
            i += 2
        return list(numsset)
                
        