class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in {'{', "[", "("}:
                stack.append(i)
            elif len(stack):
                prev = stack.pop()
                if (prev == '[' and i == ']') or \
                    (prev == '{' and i == '}')  or \
                    (prev == '(' and i == ')') :
                    continue
                else:
                    return False
            else:
                return False
        
        return len(stack)==0
                
        return len(stack) == 0