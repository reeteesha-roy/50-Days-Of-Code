# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        
        length = 0
        current = head

        while current:
            length += 1
            current = current.next
        
        # Calculate the index of the middle node
        middle = length // 2
        
        # Second pass: remove the middle node
        current = head
        for i in range(middle - 1):  # Navigate to the node before the middle
            current = current.next
            
        # Remove the middle node
        current.next = current.next.next
        
        return head
