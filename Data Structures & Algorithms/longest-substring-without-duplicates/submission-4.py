class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        q = set()
        l, r = 0, 0
        maxl = 0
        while r < len(s):
            if s[r] not in q:
                q.add(s[r])
                maxl = max(maxl, len(q))
                r+=1
            else:
                while s[r] in q:
                    q.remove(s[l])
                    l+=1
        return maxl