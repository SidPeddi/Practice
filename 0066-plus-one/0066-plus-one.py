class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        else:
            digits = digits[::-1]
            x = 0
            while x < len(digits):
                if x + 1 != len(digits) and digits[x] == 9:
                    digits[x] = 0
                    if digits[x+1] != 9:
                        digits[x+1] += 1
                        break
                    else:
                        x += 1
                if x + 1 == len(digits) and digits[x] == 9:
                    digits[x] = 0
                    digits.append(1)
                    break
            return digits[::-1]
                    
                    
                    
                
        