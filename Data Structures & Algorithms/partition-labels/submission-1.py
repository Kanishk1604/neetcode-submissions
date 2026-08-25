class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        intervalMap = defaultdict(list)

        for i in range(len(s)):
            c = s[i]
            if not intervalMap[c]:
                intervalMap[c] = [i, i]
            else:
                intervalMap[c][1] = i
            
        intervals = list(intervalMap.values())
        res = []
        res.append(intervals[0])

        for i in range(1, len(intervals)):
            last = res[-1][1]

            start, end = intervals[i]       #[0,3] [1, 4]   -> [0, 4]  [5, 9] [10,10]

            if last > start:
                res[-1][1] = max(last, end)
            else:
                res.append([start, end])

        answer = []
        for start, end in res:

            answer.append(end - start + 1)

        return answer



