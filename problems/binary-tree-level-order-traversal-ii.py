class Solution:
    ```
    First solution uses recursion
    ```
    #def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
    #    self.traversal = []
    #    self.helper(root, 0)
    #    return reversed(self.traversal)
        
    #def helper(self, node, level):
    #    if not node:
    #        return
    #    if len(self.traversal) <= level:
    #        self.traversal.append([])
    #    self.traversal[level].append(node.val)
    #    self.helper(node.left, level + 1)
    #    self.helper(node.right, level + 1)
    #    return
    
    ```
    Second solution does a dfs using a stack.
    ```
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:    
        traversal = []
        stack = [(root, 0)]
        while stack:
            node, level = stack.pop()
            if not node: 
                continue
            if len(traversal) <= level:
                traversal.append([])
            traversal[level].append(node.val)
            stack.append((node.right, level + 1))
            stack.append((node.left, level + 1))
        return reversed(traversal)
