class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            for x in range(n):
                nums1.pop(0)
                nums1.append(nums2[x])
            return
        if n == 0:
            return
        
        
        i = 0
        j = 0
        while i < (m+n) and j < n:
            if nums1[i] > nums2[j]:
                nums1.insert(i,nums2[j])
                j += 1
            i += 1
        for x in range(n):
            nums1.pop() 
        if nums2:
            for x in range(j,n):
                nums1.append(nums2[x])
              
        return 
        
        