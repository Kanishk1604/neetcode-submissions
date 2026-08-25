class Solution:
    def checkValidString(self, s: str) -> bool:
        stk = []
        starStk = []

        for i in range(len(s)):
            c = s[i]
            if c == "(":
                stk.append(i)
            elif c == "*":
                starStk.append(i)
            else:
                if stk:
                    stk.pop()
                elif starStk:
                    starStk.pop()
                else:
                    return False

        while stk and starStk:
            if stk.pop() > starStk.pop():
                return False
        
        return not stk