class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {'(': ')', '[': ']', '{': '}'}

        for i in range(len(s)):
            c = s[i]
            if c in brackets:
                stack.append(c)
            else:
                if len(stack)==0:
                    return False
                if brackets[stack[-1]] == c:
                    stack.pop()
                else:
                    return False
                
        return True if len(stack)==0 else False