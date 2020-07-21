class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0,head)
        node = dummy
        while node.next:
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next
            
        return dummy.next
