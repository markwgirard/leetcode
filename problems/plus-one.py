class Solution:
    # The fast solution.
    #def plusOne(self, digits: List[int]) -> List[int]:
    #    i = len(digits) - 1
    #    while digits[i] == 9:
    #        digits[i] = 0
    #        i -= 1
    #        if i < 0: return [1] + digits
    #    digits[i] += 1
    #    return digits
    
    
    # The one-liner solution.
    def plusOne(self, digits: List[int]) -> List[int]:
        return map(int,str(int(''.join(map(str,digits)))+1))
