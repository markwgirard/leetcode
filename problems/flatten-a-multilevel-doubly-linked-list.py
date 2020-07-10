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
