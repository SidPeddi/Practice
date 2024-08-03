class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        ans = {}
        count = 0
        for x in time:
            tempsum = x % 60
            if tempsum != 0:
                if (60 - (tempsum)) in ans:
                    count += ans[60-tempsum]
                ans[tempsum] = ans.get(tempsum,0) + 1
            else:
                if ((tempsum)) in ans:
                    count += ans[tempsum]
                ans[tempsum] = ans.get(tempsum,0) + 1
        return count
            
        