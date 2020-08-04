class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num&(num-1) == 0 and num%3==1
