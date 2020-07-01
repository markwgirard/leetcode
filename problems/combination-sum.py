class Solution:
    sols = set()
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.sols = set()
        candidates.sort()
        self.helper([],candidates,target)
        return self.sols
    
    def helper(self,included,candidates,remainder):
        if remainder == 0: 
            self.sols.add(tuple(included))
        for i in range(len(candidates)):
            c = candidates[i]
            k = 1
            while k*c <= remainder:
                self.helper(included + [c]*k, candidates[i+1:], remainder - c*k)
                k += 1
        return
