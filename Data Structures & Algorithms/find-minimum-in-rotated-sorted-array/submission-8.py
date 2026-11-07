class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        mid = l + (r - l)//2
        minimum = nums[mid]
        while l<r:
            if nums[mid] > nums[r]: #krenuo je posle sredine
                # 3 4 5 6 7 1 2 
                # 6 7 1 2 3 4 5
                l = mid + 1
            if nums[mid] <= nums[r]: # krenuo je posle
                r = mid - 1
            mid = l + (r - l)//2
            minimum = min(minimum, nums[mid])
        return minimum
        
        
                
