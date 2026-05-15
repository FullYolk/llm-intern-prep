class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        p_count = {}
        s_count = {}
        result = []
        for ch in p:
            if ch not in p_count:
                p_count[ch] = 1
            else:
                p_count[ch] += 1
        for i in range(len(p)):
            if s[i] not in s_count:
                s_count[s[i]] = 1
            else:
                s_count[s[i]] += 1
        if p_count == s_count:
            result.append(0)
        for i in range(len(p),len(s)):
            if s[i] not in s_count:
                s_count[s[i]] = 1
            else:
                s_count[s[i]] += 1
            s_count[s[i-len(p)]] -= 1
            if s_count[s[i-len(p)]] == 0:
                s_count.pop(s[i-len(p)])
            if p_count == s_count:
                result.append(i-len(p)+1)
        return result
    
#Python的range不包含右边界
#可以用from collections import Counter

# 这下面两行，等价于你开头手写的那 10 多行循环！
#p_count = Counter(p)
#s_count = Counter(s[:len(p)])