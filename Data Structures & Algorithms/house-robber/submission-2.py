class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        money = [-1] * n

        def dfs(i):
            if i>=n:
                return 0
            if money[i] != -1:
                return money[i]
            money[i] = nums[i] + max(dfs(i+2), dfs(i+3))
            return money[i]
        
        return max(dfs(0), dfs(1))