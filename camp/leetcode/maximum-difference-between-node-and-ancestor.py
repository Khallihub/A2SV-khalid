# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        max_abs = 0
        def helper(root, max_, min_):
            if root is None: return 0
            
            max_ = max(root.val, max_)
            min_ = min(root.val, min_)
            
            nonlocal max_abs
            max_abs = max(max_abs, max_ - min_)

            left = helper(root.left, max_, min_)
            right = helper(root.right, max_, min_)

        helper(root, float("-inf"), float("inf"))
        return max_abs