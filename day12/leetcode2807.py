# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            # If the list is empty or has only one node, nothing to insert
            return head
        
        current = head
        
        # Traverse the linked list
        while current and current.next:
            next_node = current.next
            
            # Calculate the GCD of the current node value and the next node value
            gcd_value = self.find_gcd(current.val, next_node.val)
            
            # Create a new node with the GCD value
            gcd_node = ListNode(gcd_value)
            
            # Insert the GCD node between current and next_node
            current.next = gcd_node
            gcd_node.next = next_node
            
            # Move to the node after the inserted GCD node
            current = next_node
        
        return head
    
    def find_gcd(self, a: int, b: int) -> int:
        
        # Euclidean algorithm implementation
        while b:
            a, b = b, a % b
        return a
