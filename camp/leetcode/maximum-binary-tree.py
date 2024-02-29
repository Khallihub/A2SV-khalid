# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None


        middle = max(nums)
        mid = nums.index(middle)

        left = self.constructMaximumBinaryTree(nums[:mid])
        right = self.constructMaximumBinaryTree(nums[mid+1:])

        return TreeNode(nums[mid], left, right)
