class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x: (x[1]))
        i = 0
        count = 0
        while i != len(points):
            selected_point = points[i][1]
            while i != len(points) and points[i][0] <= selected_point:
                i += 1
            count += 1
        return count