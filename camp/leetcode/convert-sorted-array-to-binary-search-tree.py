# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def helper(nums: List[int] , l: int,r: int) -> Optional[TreeNode]:
            if l > r:
                return
            mid = (l + r)//2
            left = helper(nums, l, mid-1)
            right = helper(nums, mid+1, r)

            return TreeNode(nums[mid], left, right)
        return helper(nums,0, len(nums)-1)