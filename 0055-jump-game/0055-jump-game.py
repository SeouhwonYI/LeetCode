class Solution:
    def canJump(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)):
            nums[i] = max(i+nums[i], nums[i-1])
        pos = 0
        while pos < len(nums)-1:
            if nums[pos] == pos:
                return False
            pos = nums[pos]
        
        return True