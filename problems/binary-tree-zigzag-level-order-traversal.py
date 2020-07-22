class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        row, out, rev = [root], [], False
        while row:
            out.append([node.val for node in (reversed(row) if rev else row)])
            rev = not rev
            row = [child for node in row for child in (node.left,node.right) if child]
        return out
