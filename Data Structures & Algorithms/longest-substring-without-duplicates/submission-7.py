class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        q = set()
        l = 0
        best = 0
        for i, char in enumerate(s):
            while char in q:
                q.remove(s[l])
                l+=1
            q.add(char)
            best = max(best, len(q))
        return best
        
