class Solution(object):
    def largestPalindromic(self, num):
        """
        :type num: str
        :rtype: str
        """
        count = Counter(num)
        nums = list(count)
        nums.sort(reverse = True)
        ans = ''
        mid = ''
        for x in nums:
            while count[x] >= 2:
                ans += x
                count[x] -= 2
        for x in nums:
            if count[x] >= 1:
                mid = x
                break
        while ans:
            if ans[0] == '0':
                ans = ans[1:]
            else:
                break

        return (ans + mid + ans[::-1]) or '0'
        