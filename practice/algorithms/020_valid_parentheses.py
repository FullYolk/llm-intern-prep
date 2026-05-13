class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "]":"[","}":"{"}
        for ch in s:
            if ch in mapping:
                if stack:
                    c = stack.pop()
                else:
                    c = "8"
                if c is not mapping[ch]:
                    return False
            else:
                stack.append(ch)
        return not stack
        
# 先判栈空 再匹配（否则越界） 注意写法和字典查找提速