class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        h = {}
        for n in nums:
            if n in h: 
                h[n] +=1
            else: 
                h[n] = 1
        count = 0
        for n in h:
            count += h[n]*(h[n]-1)//2
        return count
