# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
         # Create a dummy node to simplify edge cases (like removing the head)
        dummy = ListNode(0)
        dummy.next = head
        fast = slow = dummy

        # Move fast n+1 steps ahead
        for _ in range(n + 1):
            fast = fast.next

        # Move both fast and slow until fast reaches the end
        while fast:
            fast = fast.next
            slow = slow.next

        # Now, slow.next is the node to remove
        slow.next = slow.next.next

        # Return the  head 
        return dummy.next
