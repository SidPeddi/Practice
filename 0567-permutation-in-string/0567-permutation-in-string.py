class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = len(s1)
        for x in range(len(s2)-r+1):
            if Counter(s1) == Counter(s2[l+x:r+x]):
                return True
        return False
            

                
            