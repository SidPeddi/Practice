class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
      
        temp = []
        ans = []
        count = 0
        for x in range(len(grid)):
            for i in range(len(grid)):
                temp.append(grid[i][x])
            ans.append(temp)
            temp = []
        for x in grid:
            for j in ans:
                if x == j:
                    count += 1
        return count
        