class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        max_palindrome = ''
        for i in range(2*n-1):
            if i % 2:
                lo, hi = i//2, (i+1)//2
                palindrome = ''
            else:
                lo, hi = i//2 - 1, i//2 + 1
                palindrome = s[i//2]
            while 0 <= lo and hi <= n-1 and s[lo] == s[hi]:
                palindrome = s[lo] + palindrome + s[hi]
                lo, hi = lo - 1, hi + 1
            if len(palindrome) > len(max_palindrome):
                max_palindrome = palindrome
        return max_palindrome
