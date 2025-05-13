class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        # Dummy heads for two partitions
        less_head = ListNode(0)
        greater_head = ListNode(0)

        # Tails for building the lists
        less = less_head
        greater = greater_head

        current = head
        while current:
            if current.val < x:
                less.next = current
                less = less.next
            else:
                greater.next = current
                greater = greater.next
            current = current.next

        # Finish the second list
        greater.next = None

        # Connect the two partitions
        less.next = greater_head.next

        return less_head.next

