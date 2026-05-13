from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        num_set = set(nums)
        for i in num_set:
            cur_len = 1
            num = i
            if (num-1) not in num_set:
                while (num + 1) in num_set:
                    num = num + 1
                    cur_len = cur_len + 1
                if cur_len >= max_len:
                    max_len = cur_len
        return max_len



