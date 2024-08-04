class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        ans = []
        for l in range(len(nums)):
            temp = [nums[l]]
            for r in range(l+1,len(nums)):
                temp.append(temp[-1] + nums[r])
            l += 1
            ans += temp
        ans.sort()

        return sum(ans[left-1:right]) % (10**9 + 7)
        