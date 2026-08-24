class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [nums.index(target), sorted(nums).index(target)+1 if nums.index(target)==sorted(nums).index(target) else sorted(nums).index(target)] if target in nums else [-1, -1]