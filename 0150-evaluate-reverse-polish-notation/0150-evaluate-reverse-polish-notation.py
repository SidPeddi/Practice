class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for x in tokens:
            if x == '+' or x == '-' or x == '*' or x == '/':
                temp1 = int(stack.pop())
                temp2 = int(stack.pop())
                if x == '+':
                    stack.append(temp2 + temp1)
                if x == '-':
                    stack.append(temp2 - temp1)
                if x == '*':
                    stack.append(temp2 * temp1)
                if x == '/':
                    stack.append(temp2 / temp1)
            else:
                stack.append(x)
        return int(stack.pop())