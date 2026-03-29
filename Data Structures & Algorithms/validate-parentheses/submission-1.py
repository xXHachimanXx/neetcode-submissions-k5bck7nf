class Solution:
    def isValid(self, s: str) -> bool:
        # parentheses, brackets and braces
        # (){()}[
        # if is not the same type or the stack is not empty, return FAlse

        op = set(['(', '[', '{'])
        cl = set([')', ']', '}'])

        paren = set(['(', ')'])
        brack = set(['[', ']'])
        braces = set(['{', '}'])

        stack = []

        for char in s:
            if char in op:
                stack.append(char)
            elif len(stack) == 0:
                return False
            elif (stack[-1] in paren and char in paren) or (stack[-1] in brack and char in brack) or (stack[-1] in braces and char in braces):
                stack.pop()
            else:
                return False

        print(stack)
        return len(stack) == 0

        