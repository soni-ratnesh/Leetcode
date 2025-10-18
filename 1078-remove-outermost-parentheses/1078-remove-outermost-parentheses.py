class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        is_start = 1

        result = []
        for ii in s:
            if is_start:
                is_start=0
                continue
            elif ii == '(':
                stack.append(ii)
                result.append(ii)
            elif len(stack) and ii == ')':
                stack.pop()
                result.append(ii)
            else:
                is_start=1
            
        return "".join(result)
        