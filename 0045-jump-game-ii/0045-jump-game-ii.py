class Solution:
    def jump(self, nums: List[int]) -> int:
        # affordable max distance
        for i in range(1, len(nums)):
            nums[i] = max(i+nums[i], nums[i-1])
        cnt = 0
        pos = 0
        while pos < len(nums)-1:
            cnt += 1
            pos = nums[pos]
        return cnt