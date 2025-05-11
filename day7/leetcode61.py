# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        #  Get the length and tail of the list
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # Optimize k
        k = k % length
        if k == 0:
            return head

        # Find the new tail and new head
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next
        new_head = new_tail.next

        # Break the list and reconnect
        new_tail.next = None
        tail.next = head

        return new_head

        
