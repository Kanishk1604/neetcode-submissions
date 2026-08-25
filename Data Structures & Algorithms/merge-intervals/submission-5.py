class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        res = []
        res.append(intervals[0])

        for i in range(1, len(intervals)):
            last = res[-1][1]

            start, end = intervals[i]

            if last >= start:
                res[-1][1] = max(last, end)
            else:
                res.append([start, end])

        return res