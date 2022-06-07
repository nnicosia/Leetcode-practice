class Solution:
    def evalRPN(self, tokens) -> int:
        stack = []
        for t in tokens:
            if t == "+":
                stack.append(stack.pop() + stack.pop())
            elif t == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif t == "*":
                stack.append(stack.pop() * stack.pop())
            elif t == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(t))
        return stack.pop()

test = Solution()
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(test.evalRPN(tokens))

