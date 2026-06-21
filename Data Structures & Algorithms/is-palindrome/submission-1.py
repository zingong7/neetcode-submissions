class Solution:
    def isPalindrome(self, s: str) -> bool:
        concatstring="".join(char for char in s if char.isalnum())
        reversestring=concatstring[::-1]
        return concatstring.lower()==reversestring.lower()