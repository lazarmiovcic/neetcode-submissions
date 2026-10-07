class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r: 
            guess = l + (r-l) // 2
            if nums[guess] == target:
                return guess
            elif nums[guess] < target:
                l = guess + 1 
            else:
                r = guess - 1 
                
        return -1