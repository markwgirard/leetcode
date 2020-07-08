class Solution:
    # Stack, breadth-first search
    #def rightSideView(self, root: TreeNode) -> List[int]:
    #    if not root: return []
    #    ans, bfs = [], [root]
    #    while bfs:
    #        ans.append(bfs[-1].val)
    #        bfs = [child for node in bfs for child in (node.left,node.right) if child]
    #    return ans

    # Recursion, depth-first search
    def rightSideView(self, root: TreeNode) -> List[int]:    
        self.ans = []
        self.dfs(root,0)
        return self.ans
        
    def dfs(self,node,level):
        if not node: return
        if level >= len(self.ans):
            self.ans.append(node.val)
        self.dfs(node.right, level + 1)
        self.dfs(node.left, level + 1)
        return
