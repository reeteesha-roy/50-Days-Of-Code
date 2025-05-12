class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # Dummy node to act as the head of the new list
        dummy = ListNode(0)
        dummy.next = head
        
        # prev is the last node in the result list
        prev = dummy
        current = head
        
        while current:
            # Check for duplicates
            if current.next and current.val == current.next.val:
                # Skip all nodes with the same value
                dup_val = current.val
                while current and current.val == dup_val:
                    current = current.next
                # prev.next skips all dups
                prev.next = current
            else:
                # No duplicate, move prev forward
                prev = prev.next
                current = current.next
        
        return dummy.next
