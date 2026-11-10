class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums = sorted(nums)

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            target = -nums[i]
            l, r = i + 1, len(nums) - 1
            while l < r:
                guess = nums[l] + nums[r]
                if guess > target:
                    r-=1
                elif guess < target:
                    l+=1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l,r = l+1,r-1
                    while l<r and nums[l-1] == nums[l]:
                        l+=1
                    while l<r and nums[r+1]==nums[r]:
                        r-=1
        return res