class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        letters = []    #convert to str

        digitMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        def dfs(i):
            if i >= len(digits):
                res.append("".join(letters))
                return
            
            for j in digitMap[digits[i]]:
                letters.append(j)
                dfs(i + 1)
                letters.pop()

        dfs(0)
        return res