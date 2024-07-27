class Solution:
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()   
        result = [intervals[0]]
        
        for interval in intervals[1:]:
            interval_2 = result[-1]
            
            if interval_2[1] >= interval[0]:
                merged_back = max(interval[1], interval_2[1])
                result[-1][1] = merged_back
            else:
                result.append(interval)               
        
        return result