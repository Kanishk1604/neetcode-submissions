class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digitMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        subset = []
        res = []

        def dfs(i):
            if i >= len(digits):
                res.append("".join(subset.copy()))
                return 
            
            for j in digitMap[digits[i]]:
                subset.append(j)
                dfs(i + 1)
                subset.pop()
        
        dfs(0)
        return res