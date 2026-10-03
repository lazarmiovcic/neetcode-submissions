class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        curr_max = 0
        while l < r:
            w = r-l
            h = min(heights[l], heights[r])
            vol = h * w
            if vol > curr_max:
                curr_max = vol
            if heights[l] == h:
                l+=1
            else:
                r-=1
        
        return curr_max