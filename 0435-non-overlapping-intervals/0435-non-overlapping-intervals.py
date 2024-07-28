class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 1
        intervals.sort(key=lambda x: (x[1]))
        
        prev = 0
        for i in range(1,len(intervals)):
            if intervals[i][0] >= intervals[prev][1]:
                prev = i
                count += 1
        return len(intervals) - count
        