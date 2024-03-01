# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        def inOrder(root):
            if root == None:
                return []
            if root == None:
                return []
            left = inOrder(root.left)
            right = inOrder(root.right)
            return [*left,root.val, *right]

        nodes = inOrder(root)

        def helper(nodes, l, r):
            if l > r:
                return 

            mid = (l+r)//2

            left = helper(nodes, l, mid-1)
            right = helper(nodes, mid+1, r)

            return TreeNode(nodes[mid], left, right)

        return helper(nodes,0, len(nodes)-1)
        