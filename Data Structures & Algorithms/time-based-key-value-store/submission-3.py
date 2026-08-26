class TimeMap:

    def __init__(self):
        self.keyValueMap = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keyValueMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if not self.keyValueMap[key]:
            return ""
        intervals = self.keyValueMap[key]
        n = len(intervals)
        l, r = 0, n - 1
        res = ""
        while l <= r:
            mid = (l + r) // 2
            if intervals[mid][0] <= timestamp:
                res = intervals[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return res
