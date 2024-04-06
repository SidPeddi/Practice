class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        temp = set(nums)
        ans = 0
        for x in temp:
            if (x - 1) not in temp:
                counter = 0
                while (x + counter) in temp:
                    counter += 1
                ans = max(ans,counter)
        return ans
        