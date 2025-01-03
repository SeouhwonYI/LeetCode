class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        criterion = sum(nums) / 2
        cumsum = 0
        cnt = 0
        for i in range(0, len(nums)-1):
            cumsum += nums[i]
            if cumsum >= criterion:
                cnt += 1

        return cnt