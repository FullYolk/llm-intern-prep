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
                if c != mapping[ch]: #Python中 is比较的是对象身份（是否同一内存地址） ==比较的是值
                    return False
            else:
                stack.append(ch)
        return not stack
        
# 先判栈空 再匹配（否则越界） 注意写法和字典查找提速