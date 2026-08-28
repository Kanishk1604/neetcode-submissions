class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int: 
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        q = deque([beginWord])
        res = 0

        while q:
            res += 1
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for c in range(len(word)):
                    for j in range(97, 123):
                        if word[c] != chr(j):
                            newWord = word[:c] + chr(j) + word[c+1:]
                            if newWord in wordSet:
                                q.append(newWord)
                                wordSet.remove(newWord)
                                
        return 0