class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = set()
        max_length = 0
        left = 0
        for right in range(len(s)):
            while s[right] in dic:
                dic.remove(s[left])
                left += 1
            dic.add(s[right])
            length = right - left + 1
            if length > max_length:
                max_length = length
        return max_length
