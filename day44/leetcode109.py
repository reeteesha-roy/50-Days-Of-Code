class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        # Convert linked list to array
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        
        # Build BST from sorted array
        return self.buildBST(nums, 0, len(nums)-1)
    
    def buildBST(self, nums, left, right):
        if left > right:
            return None
        
        mid = (left + right) // 2
        root = TreeNode(nums[mid])
        root.left = self.buildBST(nums, left, mid-1)
        root.right = self.buildBST(nums, mid+1, right)
        
        return root
