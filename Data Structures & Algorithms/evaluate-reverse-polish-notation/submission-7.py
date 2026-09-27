class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = "+-*/"
        if not tokens:
            return 0
        for t in tokens:
            if t not in ops:
                stack.append(int(t))
            else:
                a = stack.pop()
                b = stack.pop()
                if t == "+":
                    stack.append(a+b)
                if t == "-":
                    stack.append(b-a)
                if t == "*":
                    stack.append(a*b)
                if t == "/":
                   stack.append(int(float(b)/a))
        return stack.pop()