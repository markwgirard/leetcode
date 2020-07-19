class Solution:
    def addBinary(self, a: str, b: str) -> str:
        out, carry = '', 0
        a, b = list(a), list(b)
        while a or b or carry:
            if a: carry += a.pop()=='1'
            if b: carry += b.pop()=='1'
            out = ('1' if carry%2 else '0') + out
            carry //= 2
        return out
