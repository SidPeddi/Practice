class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        ans = []
        st = []
        for x in range(len(intervals)):
            st.append([intervals[x][0],x])
        st.sort()
        for x in range(len(intervals)):
            target = intervals[x][1]
            left = 0
            right = len(intervals) -1
            i = float("inf")
            while left <= right:
                mid = (left + right) // 2
                if st[mid][0] >= target:
                    i = st[mid][1]
                    right = mid - 1
                else:
                    left = mid + 1
            if i == float("inf"):
                ans.append(-1)
            else:
                ans.append(i)
        return ans
        