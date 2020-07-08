class Solution:
    def threeSum(self, nums):
        if len(nums) < 3:  return []
        # First sort the list.
        nums.sort()
        # Initialize answer set.
        ans = set()
        # Every number except the last two could be the smallest element in a valid triple.
        for i, x in enumerate(nums[:-2]):
            # If we've already had a number as a smallest element, we can skip.
            if i >= 1 and x == nums[i-1]:
                continue
            # Make hash table of values -(x+y) for all y's that appear after x.
            # If y is in table already, then we have a valid tuple and add it to the set.
            # Otherwise add -(x+y) to the table.
            d = {}
            for y in nums[i+1:]:
                if y in d:
                    z=y
                    ans.add((x, -x-z, z))
                else:
                    d[-x-y] = 1
        # Convert valid tuples to lists and return list of valid tuples.            
        return map(list, ans)
