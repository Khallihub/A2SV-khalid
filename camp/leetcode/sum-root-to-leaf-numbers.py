# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            if root is None:
                return []

            left = helper(root.left)
            right = helper(root.right)

            for i in range(len(left)):
                left[i] = str(root.val) + left[i]
            for i in range(len(right)):
                right[i] = str(root.val) + right[i]
            
            if not left and not right:
                return [str(root.val)]
            
            return [*left, *right]

        res = helper(root)
        print(res)
        total = 0
        for i in res:
            total += int(i)
        return total