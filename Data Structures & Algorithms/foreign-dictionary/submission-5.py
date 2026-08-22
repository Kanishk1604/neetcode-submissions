class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        letterMap = {c: set() for w in words for c in w}
        indegreeMap = {c: 0 for c in letterMap}
        res = []
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minlength = min(len(w1), len(w2))
            if w1[:minlength] == w2[:minlength] and len(w2) < len(w1):
                return ""
            for j in range(minlength):
                if w1[j] != w2[j]:
                    if w2[j] not in letterMap[w1[j]]:
                        letterMap[w1[j]].add(w2[j])
                        indegreeMap[w2[j]] += 1
                    break

        q = deque([i for i in indegreeMap if indegreeMap[i] == 0]) 

        while q:
            letter = q.popleft()
            res.append(letter)
            for nei in letterMap[letter]:
                indegreeMap[nei] -= 1
                if indegreeMap[nei] == 0:
                    q.append(nei)
        
        if len(res) != len(indegreeMap):
            return ""
        return "".join(res)

            
            
