class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        sreversed = s[::-1]
        count = 0
        for i in range(len(sreversed)):
            if sreversed[i].isalnum():
                count += 1
            else:
                if count:
                    return count
        return count
  
                
            
        