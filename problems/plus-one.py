class Solution:
    # The fast solution.
    #def plusOne(self, digits: List[int]) -> List[int]:
    ```
    Stops at the first digit that is not a 9 and adds 1. Otherwise, turn the 9's into 0's. If every digit turns into a zero, return [1,0,...,0].
    ```
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
