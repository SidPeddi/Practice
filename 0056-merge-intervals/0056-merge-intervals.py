class Solution:
    
    def do_overlap(self,interval_1, interval_2):
        front = max(interval_1[0],interval_2[0])
        back = min(interval_1[1], interval_2[1])      
        return back - front >= 0
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()   
        result = [intervals[0]]
        for interval in intervals[1:]:
            interval_2 = result[-1]
            
            if self.do_overlap(interval, interval_2):
                merged_front = min(interval[0], interval_2[0])
                merged_back = max(interval[1], interval_2[1])
                result[-1] = [merged_front, merged_back]
            else:
                result.append(interval)               
        return result