class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #                  i  
        # [30,38,30,36,35,40,28]
        # [30, ]
        # [1]
        # 

        n   = len(temperatures) 
        res = [0]*n
        stack = []

        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                stack_index, stack_temp = stack.pop()
                res[stack_index] = index - stack_index

            stack.append((index, temp))
                    
        return res
                


            