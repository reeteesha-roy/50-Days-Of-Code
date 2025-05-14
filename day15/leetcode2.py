# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)  # Dummy node to simplify the code
        current = dummy_head
        carry = 0

        # Traverse through both linked lists
        while l1 or l2 or carry:
            # Get values from the current nodes of both lists, if present, otherwise 0
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate the sum and the new carry
            total = val1 + val2 + carry
            carry = total // 10  # Carry will be the quotient
            current.next = ListNode(total % 10)  # Create new node with the remainder
            current = current.next  # Move to the next node

            # Move to the next nodes in the input lists, if present
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy_head.next  # Return the next node after the dummy head
