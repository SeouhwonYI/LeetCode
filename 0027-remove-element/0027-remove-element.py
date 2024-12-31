class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        maps = {val:[]}
        cnt = 0
        for i in range(len(nums)):
            if nums[i] == val:
                cnt += 1
                maps[val].append(i)
        
        idx = len(nums)-1
        while maps[val]:
            while idx in maps[val]:
                idx -= 1
            put = maps[val].pop(0)
            nums[put] = nums[idx]
            idx -= 1
        
        return len(nums)-cnt

        
