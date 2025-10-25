class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []
        for ele in asteroids:
            
            while len(stack) and ele<0<stack[-1]:
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

                
                
                    