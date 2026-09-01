class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = []
        self.timeMap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        res = ""
        timeList = self.timeMap.get(key, [])

        l, r = 0, len(timeList) - 1

        while l <= r:
            mid = (l + r) // 2

            if timeList[mid][1] <= timestamp:
                res = timeList[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        
        return res
