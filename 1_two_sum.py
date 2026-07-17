class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        if len(nums)==2:
            return [0, 1]

        nums_without_current_index = nums.copy()
        
        for i in nums:
            nums_without_current_index.pop(nums.index(i))
            for j in nums_without_current_index:
                if i+j == target:return [nums.index(i), nums_without_current_index.index(j)+1] 
            nums_without_current_index = nums.copy()