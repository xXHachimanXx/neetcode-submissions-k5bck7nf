# class Solution:


#     def evalRPN(self, tokens: List[str]) -> int:
#         # ["1","2","+","3","*","4","-"]
#         # [5]

#         def operate(stack, op):

#             res = stack.pop(0)
#             while len(stack) > 0:
#                 if op == '+': 
#                     res = res + stack.pop(0)
#                 elif op == '-':
#                     res = res - stack.pop(0)
#                 elif op == '*':
#                     res = res * stack.pop(0)
#                 elif op == '/':
#                     res = res // stack.pop(0)

#             return res

#         stack = []

#         for token in tokens:
#             if token.isnumeric():
#                 stack.append(int(token))
#             else:
#                 res = operate(stack, token)
#                 stack.append(res)

#         return stack[0]
            
class Solution:


    def evalRPN(self, tokens: List[str]) -> int:
        # ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
        # []

        def operate(v1, v2, op):
            if op == '+': 
                return v1 + v2
            elif op == '-':
                return v1 - v2
            elif op == '*':
                return v1 * v2
            elif op == '/':
                return int(v1/v2)

        stack = []

        for token in tokens:
            if token.lstrip("-").isdigit():
                stack.append(int(token))
            else:
                v2 = stack.pop()
                v1 = stack.pop()
                res = operate(v1, v2, token)
                stack.append(res)

        return stack[0]
            