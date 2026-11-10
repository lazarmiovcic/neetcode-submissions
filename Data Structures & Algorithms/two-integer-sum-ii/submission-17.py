class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            guess = numbers[r] + numbers[l]
            while guess < target:
                l+=1
                guess = numbers[r] + numbers[l]
            if guess == target:
                return [l+1,r+1]
            else:
                r-=1
        return []