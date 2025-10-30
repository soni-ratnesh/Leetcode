class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        result=[]
        for ele in s:
            if ele == ']':
                # pop till '[' found
                c = []
                while stack[-1] != '[':
                    c.append(stack.pop())
                stack.pop()
                # pop till non number found
                n = []
                while stack and stack[-1].isnumeric():
                    n.append(stack.pop())
                # create string
                r = "".join(c[::-1]) * int("".join(n[::-1]))
                stack.append(r)
            else:
                stack.append(ele)
        return "".join(stack)