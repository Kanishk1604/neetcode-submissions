class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #sort with 2nd key
        # compare start < last
        # store min of end, last
        # to minimize no of intervals removed
        #else append 
        #store in arr to get the last interval retrieved
        if len(intervals) == 1:
            return 0
        intervals.sort(key = lambda i: i[1])
        newInterval = []
        newInterval.append(intervals[0])
        res = 0
        for start, end in intervals[1:]:
            last = newInterval[-1][1]

            if start < last:    #overlapping
                res += 1
            else:
                newInterval.append([start, end])

        return res


