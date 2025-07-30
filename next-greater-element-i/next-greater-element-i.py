class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = {}
        stack = []
        ans = []
        for x in nums2:
            while stack and stack[-1] < x:
                hashmap[stack.pop()] = x
            stack.append(x)
        for i in nums1:
            ans.append(hashmap.get(i,-1))
        return ans