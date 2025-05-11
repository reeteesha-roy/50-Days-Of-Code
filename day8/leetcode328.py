# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Handle empty list or single node cases
        if not head or not head.next:
            return head
        
        # Initialize pointers
        odd_head = odd = head  # First node (index 1) is odd
        even_head = even = head.next  # Second node (index 2) is even
        
        # Traverse the list and group nodes
        while even and even.next:
            # Connect odd nodes
            odd.next = even.next
            odd = odd.next
            
            # Connect even nodes
            even.next = odd.next
            even = even.next
        
        # Connect the end of odd list to the start of even list
        odd.next = even_head
        
        return odd_head
