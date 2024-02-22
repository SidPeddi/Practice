class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = defaultdict(list)
        for x in nums:
            if x in dict:
                dict[x] += 1
            else:
                dict[x] = 1
        maxi=0
        l=[]
        for i in dict:
            l.append(dict[i])
            maxi=max(maxi,dict[i])
        return l.count(maxi)*maxi

        