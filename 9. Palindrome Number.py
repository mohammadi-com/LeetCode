class Solution:
    def isPalindrome(self, x: int) -> bool:
        number_str = str(x)
        for i in range(len(number_str)//2):
            if number_str[i] != number_str[len(number_str)-i-1]:
                return False
        return True
