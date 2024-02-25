# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dic = defaultdict(int)
        def helper(root):
            if root is None:
                return 0
            dic[root.val] += 1
            
            helper(root.left)
            helper(root.right)
        helper(root)
        dic = dic.items()
        s = sorted(dic, key=lambda x:x[1])
        max_ = s[-1][1]
        res = []
        for i in s:
            if i[1] == max_:
                res.append(i[0])
        return res
