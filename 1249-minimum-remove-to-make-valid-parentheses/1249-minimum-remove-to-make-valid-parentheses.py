class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        s = list(s)
        for i,v in enumerate(s):
            if not v.isalnum():
                if v == "(":
                    stack.append((i))
                if v == ")":
                    if stack:
                        stack.pop()
                    else:
                        s[i] = ''
        while stack:
            s[stack.pop()] = ''
        return ''.join(s)
        
       
                    
                
        
     