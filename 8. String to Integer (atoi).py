import re

class Solution:
    def myAtoi(self, s: str) -> int:
        match = re.fullmatch(pattern=r'\s*([+-]?\d+).*', string=s)
        if match:
            number_str = match.group(1)
            number = int(number_str)
            number = 2**31-1 if number > 2**31-1 else number
            number = -2**31 if number < -2**31 else number
            return number
        return 0