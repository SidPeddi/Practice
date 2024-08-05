class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = Counter(arr)
        for x in list(count):
            if count[x] == 1:
                if k > 1:
                    k -= 1
                else:
                    return x
        return ""
        