class Solution:
    def sumOfLeftLeaves(self, root: TreeNode, isLeft = False) -> int:
        if not root: return 0
        r,l = root.left, root.right
        if not (r or l): return root.val*isLeft
        return self.sumOfLeftLeaves(l, True) + self.sumOfLeftLeaves(r)
