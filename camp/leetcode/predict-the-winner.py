class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        if len(nums) <= 2:
            return True

        def helper(nums,turn,res):
            if len(nums) == 0: 
                return 0

            if turn:
                res += max(nums[0] + helper(nums[1:],not turn,res), nums[-1] + helper(nums[:-1],not turn,res))
            else:
                res += min(helper(nums[1:],not turn,res), helper(nums[:-1],not turn,res))
                
            
            return res

        player1 = helper(nums,True,0)
        if player1 >= sum(nums) - player1:
            return True
        return False