class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        HashMap = {}
        pairs = 0
        
        for t in time:
            numMod = t % 60
            
            if numMod == 0:
                if 0 in HashMap:
                    pairs += HashMap[0]
            elif (60 - numMod) in HashMap:
                pairs += HashMap[60 - numMod]
                
            HashMap[numMod] = HashMap.get(numMod,0) + 1

                
        return pairs