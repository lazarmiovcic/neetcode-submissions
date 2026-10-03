class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:    
        results = []
        nums = sorted(nums)
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            l, r = i + 1, len(nums) - 1
            target = -nums[i]
            
            while l < r:
                curr_sum = nums[l] + nums[r]
                if curr_sum > target:
                    r -= 1
                elif curr_sum < target:
                    l += 1
                else:
                    results.append([nums[i], nums[l], nums[r]])
                    l, r = l + 1, r - 1
                    while l < r and nums[r + 1] == nums[r]:
                        r -= 1
                    while l < r and nums[l - 1] == nums[l]:
                        l += 1
                        
        return results

        #[-4 -1 -1 0 1 2]   1