class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack: List = []

        for asteroid in asteroids:
            if len(stack) == 0:
                stack.append(asteroid)
            elif stack[-1] > 0 and asteroid < 0:
                if abs(stack[-1]) > abs(asteroid):
                    continue
                elif abs(stack[-1]) < abs(asteroid):

                    while abs(stack[-1]) < abs(asteroid) and (stack[-1] > 0 and asteroid < 0):
                        stack.pop()
                        if not stack:
                            stack.append(asteroid)
                            break
                    else:
                        if stack[-1] == asteroid:
                            stack.append(asteroid)
                        elif abs(stack[-1]) == abs(asteroid):
                            stack.pop()
                        elif stack[-1] < 0 and asteroid < 0:
                            stack.append(asteroid)
                        elif stack[-1] > 0 and asteroid > 0:
                            stack.append(asteroid)

                elif abs(stack[-1]) == abs(asteroid):
                    stack.pop()
            else:
                stack.append(asteroid)

        return stack