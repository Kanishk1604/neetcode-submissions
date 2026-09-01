class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        seenSet = set(wordList)

        if endWord not in seenSet:
            return 0

        q = deque([beginWord])
        res = 0
        while q:
            res += 1
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for i in range(len(word)):
                    for j in range(97, 123):
                        if word[i] != chr(j):
                            newWord = word[:i] + chr(j) + word[i+1:]
                            if newWord in seenSet:
                                q.append(newWord)
                                seenSet.remove(newWord)
        
        return 0