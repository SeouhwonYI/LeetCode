class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums)):
            # p+p+p > 0
            if nums[i] > 0:
                break
            # duplicate cases (left most element struggle all thing)
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # second & third item index
            low, high = i + 1, len(nums) - 1
            while low < high:
                currSum = nums[i] + nums[low] + nums[high]

                # should include smaller term
                if currSum > 0:
                    high -= 1
                # should include bigger term
                elif currSum < 0:
                    low += 1
                else:
                    result.append([nums[i], nums[low], nums[high]])
                    second, third = nums[low], nums[high]
                    # duplicate cases
                    while low < high and nums[low] == second:
                        low += 1
                    while low < high and nums[high] == third:
                        high -= 1
                    
        return result