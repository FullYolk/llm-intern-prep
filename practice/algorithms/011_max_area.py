from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        i = 0
        j = n-1
        max_area = 0
        area = 0
        while i < j:
            if height [i] > height [j]:
                area = height[j]*(j-i)
                j = j - 1
                if area > max_area:
                    max_area = area
            else:
                area = height[i]*(j-i)
                i = i + 1
                if area > max_area:
                    max_area = area
        return max_area