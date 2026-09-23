class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeKeys = {")":"(", "}":"{", "]":"["}
        for i in s:
            if i in closeKeys:
                if stack and stack[-1] == closeKeys[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return not stack