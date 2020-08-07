class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = (''.join([c for c in s if c.isalnum()])).lower()
        return a == a[::-1]
