from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nums = []
        for sets in matrix:
            for i in sets:
                nums.append(i)
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return True
            elif target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
        return False

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) * len(matrix[0]) - 1
        while left <= right:
            mid = (left + right) // 2
            row = mid // len(matrix[0])
            col = mid % len(matrix[0])
            if target == matrix[row][col]:
                return True
            elif target < matrix[row][col]:
                right = mid - 1
            elif target > matrix[row][col]:
                left = mid + 1
        return False