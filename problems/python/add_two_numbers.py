# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """Function to add two numbers together in a linked list notation

        Args:
            l1 (ListNode): Integer number 1 represented as a linked list
            l2 (ListNode): Integer number 2 represented as a linked list

        Returns:
            ListNode: the resulting sum returned as a linked list
        """
        head = ListNode(0)
        cur = head
        carry = 0
        while l1 or l2 or carry:
            # Set the value, including handling when l1 or l2 is none where we set to 0
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            # Find the value of the two nodes, and determine if there's a carry for next value
            sum_value = val1 + val2 + carry
            carry = sum_value // 10
            sum_value = sum_value % 10
            # Create node and append to the list
            node = ListNode(sum_value)
            # Move to the next ndoe in each list
            l1 = l1.next if l1 else 0
            l2 = l2.next if l2 else 0
            cur.next = node
            cur = node
        return head.next
