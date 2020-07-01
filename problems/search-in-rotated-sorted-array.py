class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if not n: return -1
        a, b = 0, n // 2
        while a != b and target != nums[a] and target != nums[b]:
            if nums[a] <= nums[b] < target or target < nums[a] <= nums[b] or nums[b] < target < nums[a]:
                a, b = b, a
            m = (a + ((b-a) % n)//2) % n
            if nums[m] == target:
                return m
            if (nums[a] <= nums[m] and not(nums[a] < target < nums[m])) or nums[m] < target < nums[b]:
                a = (m + 1) % n
            else:
                b = (m - 1) % n
        if nums[a] == target:
            return a
        elif nums[b] == target:
            return b
        else:
            return -1
        
        # Uses O(1) memory and O(logn) time
