class Solution:
    N = 10**5   
    dp = [0]*(N+1)
    if not dp[1]:
        for i in range(1,N+1):
            a = 1
            while a**2 <= i:
                if not dp[i - a**2]:
                    dp[i] = 1
                    break
                a += 1
    
    def winnerSquareGame(self, n: int) -> bool:
        return self.dp[n]
