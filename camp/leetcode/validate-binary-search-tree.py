# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return [root, root]

        if root.left and root.left.val >= root.val:
            return False
        if root.right and root.right.val <= root.val:
            return False

        left = self.isValidBST(root.left)
        right = self.isValidBST(root.right)
        if left is False:
            return False
        if right is False:
            return False
        if left[1] and root.val <= left[1].val:
            return False
        if right[0] and root.val >= right[0].val:
            return False

        if left[0] is None:
            left[0] = root
        if left[1] is None:
            left[1] = root
        if right[0] is None:
            right[0] = root
        if right[1] is None:
            right[1] = root
        
        cur = [left[0] if left[0].val < root.val else root, right[1] if right[1].val > root.val else root]    
        return cur