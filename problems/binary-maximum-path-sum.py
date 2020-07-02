class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_path_sum = float('-inf')
        self.dfs(root)
        return self.max_path_sum
        
    def dfs(self, node):
        if not node:
            return 0
        max_left = self.dfs(node.left)
        max_right = self.dfs(node.right)
        self.max_path_sum =  max(node.val + max_left + max_right, self.max_path_sum)
        return max(node.val + max_left, node.val + max_right, 0)
