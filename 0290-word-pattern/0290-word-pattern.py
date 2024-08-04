class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        maps = {}
        ans = []
        temp = ''
        for c in s:
            if c != ' ':
                temp += c
            if c == ' ':
                ans.append(temp)
                temp = ''
        ans.append(temp)
            
        for i,j in zip(pattern,ans):
            if i not in maps:
                maps[i] = j
            
            if i in maps:
                if j != maps[i]:
                    return False
        return len(set(ans)) == len(set(pattern)) and len(pattern) == len(ans)
        