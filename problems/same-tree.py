class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        levels = [[p,q]]
        while all([(a.val if a else None) == (b.val if b else None) for a,b in levels]):
            levels = [(x,y) for a,b in levels if (a and b) for x,y in [(a.left,b.left),(a.right,b.right)] ]
            if not levels:
                return True
        return False
