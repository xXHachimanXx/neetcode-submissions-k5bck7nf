import math

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # [7,4,1,0]
        # [1,2,2,1]
        # [3,5,10] -> len = 3

        cars = [(p,s) for p,s in zip(position,speed)]
        cars.sort(reverse=True)
        stack = []
        for p, s in cars:
            itrs_until_target = (target-p)/s
            stack.append(itrs_until_target)

            if len(stack) >= 2 and stack[-2] >= stack[-1]:
                stack.pop()
        
        return len(stack)


