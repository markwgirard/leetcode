
# A one-liner!
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return [ [nums[i] for i, bit in enumerate(bin(mask)[-1:1:-1]) if bit=='1'] for mask in range(1<<len(nums))]
