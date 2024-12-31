class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pnt = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[pnt] = nums[i]
                pnt += 1

        return pnt
            