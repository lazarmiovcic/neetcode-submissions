class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]
        while l<=r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            mid = l + (r-l) // 2
            res = min(nums[mid], res)
            if nums[mid] >= nums[l]: #krenuo je posle sredine
                # 3 4 5 6 7 1 2 
                # 6 7 1 2 3 4 5
                l = mid + 1
            else: # krenuo je prije sredine
                r = mid - 1
        return res
        
        
                
