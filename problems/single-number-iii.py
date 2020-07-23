class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        x = reduce(xor, nums)
        # Get least significant bit of xor
        mask = x&-x
        a, b = 0, 0
        for num in nums:
            if num&mask:
                a ^= num
            else:
                b ^= num
        return [a,b]
