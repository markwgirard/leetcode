class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0: return self.myPow(1/x, -n)
        if not (x or n): return 'undefined'
        if not x: return 0
        power, out = x, 1
        while n:
            if n%2: 
                out *= power
            n >>= 1
            power **= 2
        return out
