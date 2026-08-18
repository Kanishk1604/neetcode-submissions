class Solution:
    def checkValidString(self, s: str) -> bool:
        stk = []
        star = []
        for i, c in enumerate(s):
            if (c == "("):
                stk.append(i)
            elif (c == ")"):
                if stk:
                    stk.pop()
                elif star:
                    star.pop()
                else:
                    return False
            elif (c == "*"):
                star.append(i)
        
        while stk and star:
            if stk.pop() > star.pop():
                return False
        
        return not stk

        
