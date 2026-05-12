class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = 0
        for i,num in enumerate(nums):
            if num != 0:
                nums[i],nums[j] = nums[j], nums[i]
                j = j + 1
        