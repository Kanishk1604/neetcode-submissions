class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqmap = {}

        for num in nums:
            freqmap[num] = 1 + freqmap.get(num, 0)
        n = len(nums)
        bucket = [[] for i in range(n+1)]

        for key, val in freqmap.items():
            bucket[val].append(key)
        res = []
        for i in range(n, 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res

        return []
        