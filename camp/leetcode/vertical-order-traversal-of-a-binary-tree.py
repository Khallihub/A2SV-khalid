# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        locations = []
        def helper(root, row, col):
            if root is None:
                return
            
            left = helper(root.left, row+1, col-1)
            right = helper(root.right, row+1, col+1)

            locations.append([col, row, root.val  ])
        helper(root,0,0)
        locations.sort()
        result = []
        i = 0
        while i < len(locations):
            tmp = []
            col = locations[i][0]
            while i < len(locations) and locations[i][0] == col:
                tmp.append(locations[i][2])
                i += 1
            result.append(tmp)
        return result