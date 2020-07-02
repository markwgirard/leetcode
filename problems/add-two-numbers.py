class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = ListNode(0, None)
        node = ans
        carry = 0
        while True:
            l1 = l1 or ListNode()
            l2 = l2 or ListNode()
            n = l1.val + l2.val + carry
            node.val, carry = n % 10, n // 10
            l1 = l1.next
            l2 = l2.next
            if not (l1 or l2 or carry):
                break
            node.next = ListNode()
            node = node.next
 
        return ans
