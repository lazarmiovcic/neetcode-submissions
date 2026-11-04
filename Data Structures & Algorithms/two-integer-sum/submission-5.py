class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = set(nums)
        idx = 0
        for i, el in enumerate(nums):
            if target - el in s:
                for j in range(i+1, len(nums)):
                    if nums[j] == target - el:
                        return [i, j]
        return []