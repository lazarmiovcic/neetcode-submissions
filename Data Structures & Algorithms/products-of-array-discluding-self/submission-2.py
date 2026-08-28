class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prods1 = [0]*n
        prods2 = [0]*n
        output=[0]*n
        for i in range(n):
            if i==0: 
                prods1[i] = nums[i]
                prods2[n-i-1] = nums[n-i-1]
            else: 
                prods1[i] = nums[i] * prods1[i-1]
                prods2[n-i-1] = nums[n-i-1] * prods2[n-i]
        for i in range(n):
            if i==0:
                output[i] = prods2[i+1]
            elif i==n-1:
                output[i] = prods1[i-1]
            else:
                output[i] = prods1[i-1] * prods2[i+1]
        return output
        