# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        current = head
        length = 0
        
        while current:
            length += 1
            current = current.next
        
        # Find the kth node from the beginning
        current = head
        for i in range(1, k):
            current = current.next
        front_node = current
        
        # Find the kth node from the end (which is (length-k+1)th node from beginning)
        current = head
        for i in range(1, length - k + 1):
            current = current.next
        end_node = current
        
        # Swap the values
        front_node.val, end_node.val = end_node.val, front_node.val
        
        return head


# Alternate one-pass solution
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        # Initialize pointers
        first = head  # Will point to kth node from beginning
        second = head  # Will point to kth node from end
        current = head
        
        # Move current to the kth node from beginning
        for i in range(1, k):
            current = current.next
        
        # Save the kth node from beginning
        first = current
        
        # Move second pointer for finding kth node from end
        # The gap between current and second should be k-1 nodes
        # When current reaches the end, second will be at the kth node from end
        second_runner = head
        while current.next:
            current = current.next
            second_runner = second_runner.next
        
        # second_runner is now the kth node from the end
        second = second_runner
        
        # Swap values
        first.val, second.val = second.val, first.val
        
        return head   
