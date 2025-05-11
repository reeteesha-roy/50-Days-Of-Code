class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        # empty list or single node
        if not head or not head.next:
            return head
            
        #slow and fast pointers
        slow = head
        fast = head
        
        # Move slow one step and fast two steps
        # When fast reaches the end, slow will be at the middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # Return the middle node (or second middle if even)
        return slow
