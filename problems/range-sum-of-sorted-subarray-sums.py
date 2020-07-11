class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        cumsums = [0]+list(accumulate(nums))
        sums = sorted([cumsums[j]-cumsums[i] for i in range(n) for j in range (i+1,n+1)])
        return sum(sums[left - 1: right])%(10**9 + 7)
        
