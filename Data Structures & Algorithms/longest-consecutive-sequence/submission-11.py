class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        d = defaultdict(list)
        for e in s:
            if e-1 not in s:
                j=0
                while e + j in s:
                    d[e].append(e+j)
                    j+=1;
        
        m = 0;
        for l in d.values():
            if m < len(l):
                m = len(l)
        
        return m
            