class Solution:
    try: nums
    except:
        nums = [1]
        idx = {2:0, 3:0, 5:0}
        nexts = {2:2, 3:3, 5:5}
    
    def nthUglyNumber(self, n):
        while len(self.nums) < n: 
            next = min(self.nexts.values())
            self.nums.append(next)
            for d in [2,3,5]:
                if next == self.nexts[d]:
                    self.idx[d] += 1
                    self.nexts[d] = self.nums[self.idx[d]]*d
        return self.nums[n-1]
