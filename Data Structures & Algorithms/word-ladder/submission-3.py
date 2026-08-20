class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord:
            return 0
        
        res = 1
        q = deque([beginWord])
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        while q:
            for lvl in range(len(q)):
                word = q.popleft()
                if word == endWord: return res
                for i in range(len(word)):
                    for j in range(97, 123):
                        if word[i] == chr(j):
                            continue
                        newWord = word[:i] + chr(j) + word[i+1:]
                        if newWord in wordSet:
                            q.append(newWord)
                            wordSet.remove(newWord)
            res += 1
        
        return 0
            

