class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), key=lambda x: x[0], reverse=True)
        steps = [(target - p) / s for p, s in cars]
        
        stack = [] 
        res = 0
        for i, s in enumerate(steps):
            if not stack:
                stack.append(s)
            if s > stack[-1]:
                stack.append(s)

        return len(stack)