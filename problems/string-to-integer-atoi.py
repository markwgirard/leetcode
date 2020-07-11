class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.lstrip()
        chars = []
        print(str)
        for c in str:
            if c in '0123456789' or (len(chars)==0 and c in '-+'):
                chars.append(c)
            else:
                break
        chars = ''.join(chars)
        print(chars)
        if  chars.lstrip("-+").isdigit():
            ans = int(chars)
        else: 
            return 0
        if ((-1)*(1<<31) <= ans < (1<<31)):
            return ans
        elif ans < (-1)*(1<<31):
            return (-1)*(1<<31)
        else:
            return (1<<31) - 1
