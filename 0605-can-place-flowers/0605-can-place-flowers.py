class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                count += 1
            return count >= n
        if len(flowerbed) == 2:
            if flowerbed[1] == 0 and flowerbed[0] == 0:
                count += 1
            return count >= n
        if flowerbed[1] == 0 and flowerbed[0] == 0:
            flowerbed[0] = 1
            count += 1
        if flowerbed[len(flowerbed) - 1] ==0 and flowerbed[len(flowerbed) - 2] == 0:
            count += 1
            flowerbed[len(flowerbed) - 1] = 1
        for x in range(1,len(flowerbed) -2):
            if flowerbed[x-1] == 0 and flowerbed[x + 1] == 0 and flowerbed[x] == 0:
                count += 1
                flowerbed[x] = 1

        return count >= n
        