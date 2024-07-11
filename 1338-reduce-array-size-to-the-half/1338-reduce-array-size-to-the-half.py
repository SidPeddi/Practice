class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        length = len(arr)
        newhalf = length // 2
        counts = Counter(arr)
        ar = counts.values()
        ar.sort(reverse= True)
        
        
        for x in range(len(ar)):
            length -= ar[x]
            if length <= newhalf:
                return x + 1
            
            