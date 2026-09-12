class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = [[] for i in range(len(nums)+1)]
        counts = {}
        for num in nums:
            counts[num] = 1 + counts.get(num,0)
        
        for num, count in counts.items():
            freqs[count].append(num)
        
        results = []
        for i in range(len(freqs)-1, -1, -1):
            if len(results) >= k:
                break
            results.extend(freqs[i])

        return results