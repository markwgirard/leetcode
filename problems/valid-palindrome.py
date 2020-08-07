class Solution:
    def isPalindrome(self, s: str) -> bool:
        # one-liner
        #return (lambda a: a==a[::-1])((''.join([c for c in s if c.isalnum()])).lower())
        
        # O(1) space 
        l, r = 0, len(s) - 1
        while l < r:
            if not s[l].isalnum(): l+=1
            elif not s[r].isalnum(): r-=1
            else:
                if s[l].lower()==s[r].lower():
                    l, r = l+1, r-1
                else:
                    return False
        return True
