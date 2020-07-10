class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        stack = [head]
        prevNode = None
        while stack:
            node = stack.pop()
            if not node: continue
            node.prev = prevNode
            if prevNode:
                prevNode.next = node     
            stack.extend([node.next, node.child])
            node.child = None
            prevNode = node
        return head
    
# more compact solution
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head: return None
        stack, prevNode = [head], Node()
        while stack:
            root = stack.pop()
            stack.extend([node for node in (root.next, root.child) if node])
            root.prev, root.child, prevNode.next, prevNode = prevNode, None, root, root
        head.prev = None
        return head
