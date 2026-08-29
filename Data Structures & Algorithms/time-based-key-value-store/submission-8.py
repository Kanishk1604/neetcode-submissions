class TimeMap:

    def __init__(self):
        self.keyValueMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyValueMap:
            self.keyValueMap[key] = []
        self.keyValueMap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.keyValueMap.get(key, [])
        left, right = 0, len(values) - 1

        while left <= right:
            mid = (left + right) // 2
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        
        return res


