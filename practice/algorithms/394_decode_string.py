class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_num = 0
        current_str = ""
        for ch in s:
            if ch.isdigit():
                current_num = current_num * 10 + int(ch)
            elif ch == '[':
                stack.append((current_str,current_num))
                current_num = 0
                current_str = ""
            elif ch == ']':
                prev_str,multiplier = stack.pop()
                current_str = current_str * multiplier
                current_str = prev_str + current_str
            else:
                current_str = current_str + ch
        return current_str

