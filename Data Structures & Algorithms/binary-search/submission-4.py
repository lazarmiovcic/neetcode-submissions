class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:  # Fixed: <= to include single-element ranges
            guess = l + (r - l) // 2
            
            if nums[guess] == target:
                return guess
            elif nums[guess] < target:
                l = guess + 1  # Target is larger, search right half
            else:
                r = guess - 1  # Target is smaller, search left half
                
        return -1