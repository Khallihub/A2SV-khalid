# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        vals = []

        def helper(root,k):
            if root is None:
                return []
            nonlocal vals

            left = helper(root.left,k)
            right = helper(root.right,k)

            return [*left, root.val, *right]
        kth = helper(root, k)
        return kth[k-1]