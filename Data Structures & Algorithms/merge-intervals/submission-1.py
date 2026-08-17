class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        if len(intervals) == 1:
            return intervals
        intervals.sort(key = lambda i: i[0])
        res.append(intervals[0])
        
        for start, end in intervals[1:]:
            last = res[-1][1]

            if start <= last:
                res[-1][1] = max(end, last)
            else:
                res.append([start, end])

        return res