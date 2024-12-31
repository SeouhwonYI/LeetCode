class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # for i in range(1, len(nums)):
        #     nums[i] = max(i+nums[i], nums[i-1])
        # pos = 0
        # while pos < len(nums)-1:
        #     if nums[pos] == pos:
        #         return False
        #     pos = nums[pos]
        
        # return True

        gas = 0
        for n in nums:
            # can't progress
            if gas < 0:
                return False
            # n: new gas vs gas: current gas
            elif n > gas:
                gas = n
            # can reach 'n' but 
            gas -= 1
            
        return True