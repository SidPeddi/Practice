class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for i in range(len(s[::-1])):
            if s[::-1][i].isalnum():
                count += 1
            else:
                if count:
                    return count
        return count
  
                
            
        