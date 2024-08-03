class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        counts = collections.Counter(arr)

        for num in sorted(arr, key=abs):
            if counts[num] == 0:
                continue
            if num*2 in counts:
                counts[num] -= 1
                counts[num*2] -= 1

        for x in list(counts):
            if counts[x] != 0:
                return False
        return True
