"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) == 0 or len(intervals) == 1:
            return True
        intervals.sort(key = lambda i: i.start)
        checkInterval = intervals[0]

        for i in range(1, len(intervals)):
            if checkInterval.end > intervals[i].start:
                return False
            else:
                checkInterval = intervals[i]
        
        return True
