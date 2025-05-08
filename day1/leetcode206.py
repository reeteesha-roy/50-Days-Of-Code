class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # Handle empty list or single node
        if head is None or head.next is None:
            return head

        # Initialize pointers
        prev = None
        current = head

        # Iterate through the list
        while current:
            # Save the next node before we change current.next
            next_temp = current.next

            # Reverse the link
            current.next = prev

            # Move pointers forward
            prev = current
            current = next_temp

        # The new head is the previous tail
        return prev
