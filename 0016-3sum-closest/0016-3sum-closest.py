class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = sum(nums[:3])

        for i in range(len(nums)):
            # duplicate cases (left most element struggle all thing)
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # second & third item index
            low, high = i + 1, len(nums) - 1
            while low < high:
                currSum = nums[i] + nums[low] + nums[high]
                # should include smaller term
                if currSum > target:
                    high -= 1
                    if currSum - target < abs(result - target):
                        result = currSum
                # should include bigger term
                elif currSum < target:
                    low += 1
                    if -currSum + target < abs(result - target):
                        result = currSum
                else:
                    return target
                    
        return result