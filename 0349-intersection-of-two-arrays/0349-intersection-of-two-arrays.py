class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = set()
        if len(nums1) > len(nums2):
            for a in nums2:
                if a in nums1:
                    ans.add(a)
        else:
            for a in nums1:
                if a in nums2:
                    ans.add(a)
        return ans
            