class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        boxTypes.sort(key = lambda x: x[1], reverse = True)
        weight = 0
        l = 0
        while truckSize and l < len(boxTypes):
            if boxTypes[l][0] <= truckSize:
                truckSize -= boxTypes[l][0]
                weight += (boxTypes[l][0] * boxTypes[l][1])
            else:
                weight += (truckSize * boxTypes[l][1])
                truckSize = 0
            l += 1
            
        return weight