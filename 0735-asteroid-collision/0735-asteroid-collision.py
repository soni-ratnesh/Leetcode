class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []
        for ele in asteroids:
            if len(stack)==0 or ele>0:
                stack.append(ele)
            else:
                while len(stack) and stack[-1]*ele<0:
                    if abs(stack[-1]) < abs(ele):
                        stack.pop()
                    elif abs(stack[-1]) == abs(ele):
                        stack.pop()
                        break
                    else:
                        break   
                else:
                    stack.append(ele)   
        return stack

                
                
                    