class Solution:
    def convert(self, s: str, numRows: int) -> str:
        output = ""
        step = 2*numRows - 2
        j = 0

        if step == 0:
            return s
        

        for i in range(numRows):
            if i == 0 or i == numRows-1:
                output += s[i::step]
            else:
                j = 0
                while step-i+j*step < len(s):
                    output += s[i+j*step] + s[step-i+j*step]
                    j += 1
                if i+j*step < len(s):
                        output += s[i+j*step]

        return output