class Solution:
    def isPalindrome(self, s: str) -> bool:

        new_word = "".join(char for char in s if char.isalnum()).lower()
        left = 0
        right = len(new_word) -1

        while left < right:
            if new_word[left] != new_word[right]:
                return False
            left += 1
            right -= 1

        return True
