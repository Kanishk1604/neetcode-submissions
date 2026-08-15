class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #set of wordlist
        # for each char in beginEWord
            # we go from a -z 
            # swap char with a-z 
            # check if new word == endword return map[newword]
            # if new word is in wordlist
            #add that new word to our map of possible words 
            # once we have seen all possibilities of beginword, we remove it 
            # from our map of possible words
            #map of possible words {beginword: 1}
            #everytime we discover new word, we add map[newword] = 1 + map[beginword]
        if (endWord not in wordList) or (beginWord == endWord):
            return 0

        wordSet = set(wordList)
        q = deque([beginWord])
        res = 0
        while q:
            res += 1
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for i in range(len(word)):
                    for c in range(97, 123):
                        if chr(c) == word[i]:
                            continue
                        new_word = word[:i] + chr(c) + word[i+1:]
                        if new_word in wordSet:
                            q.append(new_word)
                            wordSet.remove(new_word)

        return 0

