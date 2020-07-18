class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        return dfs(range(1,n+1)) if n else []
    
def dfs(nums):
    return [TreeNode(val,left,right) 
                    for i, val in enumerate(nums)
                    for left in dfs(nums[:i])
                    for right in dfs(nums[i+1:])] or [None]
