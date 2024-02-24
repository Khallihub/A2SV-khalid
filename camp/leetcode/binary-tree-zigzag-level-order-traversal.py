# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def helper(root,row,dic):
            if root is None:
                return []

            dic[row].append(root.val)
            left = helper(root.left, row+1,dic)
            right = helper(root.right, row+1,dic)


            return dic
        rows = defaultdict(list)
        dic = helper(root, 0, rows)
        res = []
        for i in range(len(dic)):
            res.append(dic[i] if i%2 == 0 else dic[i][::-1])
        return res
