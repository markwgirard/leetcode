class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        loc = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[loc]:
                loc += 1
                nums[loc] = nums[i]
        return loc + 1
