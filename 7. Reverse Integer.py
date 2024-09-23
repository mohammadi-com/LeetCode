class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        if s[0] == "-":
            y = -int(s[:0:-1])
        else:
            y = int(s[::-1])
        if -2**31 <= y <= 2**31-1:
            return y
        return 0