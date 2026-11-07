class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        best = 0
        freqs = {}
        q = []
        maxf = 0
        for r, c in enumerate(s):
            freqs[c] = freqs.get(c, 0) + 1
            maxf = max(maxf, freqs[c])
            q.append(c)
            while (r - l + 1) - maxf > k:
                q.remove(s[l])
                freqs[s[l]] -= 1
                l+=1
            best = max(best, len(q))
        return best
            
            