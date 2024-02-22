class Solution(object):
    def findJudge(self, N, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        in_degree = [0] * (N + 1)
        out_degree = [0] * (N + 1)
    
    # Update the in-degree and out-degree of each person
        for a, b in trust:
            in_degree[b] += 1
            out_degree[a] += 1
    
    # Find the person with in-degree N - 1 and out-degree 0
        for i in range(1, N + 1):
            if in_degree[i] == N - 1 and out_degree[i] == 0:
                return i
    
    # If no such person is found, return -1
        return -1
    