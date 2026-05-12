class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        num_set = set(nums)
        for i in num_set:
            len = 1
            num = i
            if (num-1) not in num_set:
                while (num + 1) in num_set:
                    num = num + 1
                    len = len + 1
                if len >= max_len:
                    max_len = len
        return max_len



