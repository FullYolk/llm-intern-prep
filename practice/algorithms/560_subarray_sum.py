class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        current_sum = 0
        prefix_map = {0:1}
        result = 0
        for num in nums:
            current_sum += num
            target = current_sum - k
            if target in prefix_map:
                result += prefix_map[target]
            if current_sum in prefix_map:
                prefix_map[current_sum] += 1
            else:
                prefix_map[current_sum] = 1
        return result