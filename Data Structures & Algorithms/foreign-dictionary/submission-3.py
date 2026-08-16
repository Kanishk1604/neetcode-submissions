class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        orderMap = {c: set() for w in words for c in w}
        indegree = {c: 0 for c in orderMap}

        start_word = words[0]
        for i in range(1, len(words)):
            word = words[i]
            length = min(len(start_word), len(word))
            if len(start_word) > len(word) and word[:length] == start_word[:length]:
                return ""
            for j in range(length):
                if start_word[j] != word[j]:
                    if word[j] not in orderMap[start_word[j]]:
                        orderMap[start_word[j]].add(word[j])  
                        indegree[word[j]] += 1   
                    break 
            start_word = word

        q = deque([c for c in indegree if indegree[c] == 0])
        res = []

        while q:
            node = q.popleft()
            res.append(node)
            for nei in orderMap[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
            
        if len(res) != len(indegree):
            return ""
        
        return "".join(res)
