class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = "".join(s.lower().split(" "))
        check_string = ""
        for c in new_string:
            if c.isalnum():
                check_string += c
        

        n = len(check_string)
        l = 0
        r = n - 1
        for i in range(n//2):
            if check_string[l] != check_string[r]:
                return False
            l += 1
            r -= 1
        
        return True
            
