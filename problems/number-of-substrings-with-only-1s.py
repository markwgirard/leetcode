class Solution:
    def numSub(self, s: str) -> int:
        curr = 0
        count = 0
        N = 10**9 + 7
        for char in s:
            if char == '0':
                curr = 0
            else:
                curr += 1
                count += curr
                count %= N
        return count % N    
