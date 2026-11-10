class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort(key = lambda pair: pair[0])

        prev_start = intervals[0][0]
        prev_end = intervals[0][1]

        for start, end in intervals[1:]:
            if prev_end <= start:
                prev_end = end
            else:
                prev_end = min(prev_end,end)
                res += 1
        return res