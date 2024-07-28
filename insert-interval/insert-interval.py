class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key = lambda i: i[0])
        
        output = [intervals[0]]
        for s,e in intervals[1:]:
            last = output[-1][1]
            if last >= s:
                output[-1][1] = max(last,e)
            else:
                output.append([s,e])
        return output
        

                    