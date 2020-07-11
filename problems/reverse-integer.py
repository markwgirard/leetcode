class Solution:
    def reverse(self, x: int) -> int:
        sign = x>=0 or -1
        digits = str(sign*x)
        num  = sign*int(digits[::-1]) 
        return num if -1*(1<<31) <= num < (1<<31) else 0
