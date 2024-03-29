class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        ans=0
        while left<right:
            left=left>>1
            right=right>>1
            ans+=1
        return left<<ans    