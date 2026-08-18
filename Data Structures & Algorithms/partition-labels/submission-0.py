class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        #store start index of char
        # store last index and update on every seen
        #if any clashing index in range of another char, max of two ends + 1
        #{x: [0,3], y: [1,4], z:[5,7], b:[6,9], i:[10,10], s:[11,11], l:[12,12]}

        #overlapping intervals -> max([1],[1]) - frst[0] + 1

        indexMap = {}

        for i in range(len(s)):
            if s[i] in indexMap:
                indexMap[s[i]][1] = i
            else:
                indexMap[s[i]] = [i,i]

        startInterval = indexMap[s[0]]
        res = []
  
        for k, v in indexMap.items():
            start, end = v
            
            if startInterval[1] < start:
                res.append(startInterval[1] - startInterval[0] + 1)
                startInterval = [start, end]
            else:
                    startInterval[1] = max(startInterval[1], end)
        
        res.append(startInterval[1] - startInterval[0] + 1)

        return res
                