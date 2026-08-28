class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        letterMap = {c: set() for word in words for c in word}
        indegree = {c: 0 for c in letterMap}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minlength = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minlength] == w2[:minlength]:
                return ""
            for j in range(minlength):
                if w1[j] != w2[j]:
                    if w2[j] not in letterMap[w1[j]]:
                        letterMap[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break
        
        queue = deque([c for c in indegree if indegree[c] == 0])
        res = []

        while queue:
            letter = queue.popleft()
            res.append(letter)
            for edge in letterMap[letter]:
                indegree[edge] -= 1
                if indegree[edge] == 0:
                    queue.append(edge)
        
        if len(res) != len(indegree):
            return ""
        
        return "".join(res)