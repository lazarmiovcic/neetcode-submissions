class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}
        output = False
        for n in nums:
            if n in d.keys():
                d[n]+=1;
                output = True
            else:
                d[n] = 1;
        return output
        