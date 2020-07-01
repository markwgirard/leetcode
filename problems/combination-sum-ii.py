class Solution:
    sols = set()
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.sols = set()
        self.helper([],candidates,target)
        return self.sols
        
    def helper(self,included,candidates,remainder):
        if remainder == 0:
            self.sols.add(tuple(included))
            return
        for i in range(len(candidates)):
            c = candidates[i]
            if c <= remainder:
                self.helper(included+[c], candidates[i+1:], remainder - c)
        return
