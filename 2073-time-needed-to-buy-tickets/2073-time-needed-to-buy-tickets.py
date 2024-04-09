class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        count = 0
        for i,v in enumerate(tickets):
            print(count, i , v)
            if v >= tickets[k]:
                count += tickets[k]
                if k < i:
                    count -= 1
            else:
                count += v
        
        return count