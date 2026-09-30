class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), key=lambda x: x[0], reverse=True)
        
        stack = [] 
        for p, s in cars:
            steps = (target - p) / s
            if not stack:
                stack.append(steps)
            if steps > stack[-1]:
                stack.append(steps)

        return len(stack)