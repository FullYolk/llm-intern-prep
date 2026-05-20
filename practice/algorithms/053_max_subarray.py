from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sums = []
        max_sum = -10e4-1
        min_pre_sum= 0
        for i, num in enumerate(nums):
            if i == 0:
                sums.append(num)
            else:
                sums.append(sums[i-1]+num)

        for i in range(len(sums)):
            if sums[i] - min_pre_sum > max:
                max_sum = sums[i] - min_pre_sum
            if sums[i] < min_pre_sum:
                min_pre_sum = sums[i]
            if sums[i] > max:
                max_sum = sums[i]
            
        return max_sum
##下面是推荐的算法
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = 0
        max_sum = float('-inf')

        for num in nums:
            if current_sum < 0:
                current_sum = num
            else:
                current_sum += num
            
            if current_sum > max_sum:
                max_sum = current_sum
        return max_sum
    
##Kadane算法 DP+贪心