class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            if n % 2:
                count += 1
            n = n >> 1
        print(n >> 4)
        return count
        