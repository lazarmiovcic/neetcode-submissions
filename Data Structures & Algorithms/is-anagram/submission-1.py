class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        else:
            ds, dt = {}, {}
            for cs, ct in zip(s, t):
                ds[cs] = ds.get(cs, 0) + 1
                dt[ct] = dt.get(ct, 0) + 1
            
            return True if ds==dt else False
