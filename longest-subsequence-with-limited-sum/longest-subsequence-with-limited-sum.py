class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        answer = []
        for x in range(1,len(nums)):
            nums[x] += nums[x-1]
        print(nums)
        for x in queries:
            answer.append(bisect.bisect_right(nums, x))
        return answer
                