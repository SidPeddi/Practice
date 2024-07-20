class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        hashset = set(nums1)
        my_list = list(hashset)
        ans = 0
        for x in range(len(my_list)):
            left = x
            right = len(nums2) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums1[x] <= nums2[mid]:
                    left = mid + 1
                    ans = max(ans, mid - x)
                else:
                    right = mid - 1
            ans = max(ans, left - x - 1)
        return ans
                    
                