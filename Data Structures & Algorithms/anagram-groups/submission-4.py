class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for i, s in enumerate(strs):
            l = [0]*26
            for c in s:
                l[ord('a')-ord(c)] += 1
            d[tuple(l)].append(s)
        
        results = [l for l in d.values()]
        return results

