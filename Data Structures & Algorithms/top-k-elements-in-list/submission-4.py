class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] = 1 + counts.get(num,0)
        
        freqs = defaultdict(list)
        for num, c in counts.items():
            freqs[c].append(num)
        
        results = []
        for key, value in sorted(freqs.items(), reverse=True):
            results.extend(value)
            if len(results) >= k:
                break
        return results[:k]