class Solution:
    def isPalindrome(self, s: str) -> bool:
        for i in range(len(s)//2):
            if s[i] != s[len(s)-i-1]:
                return False
        return True

    def longestPalindrome(self, s: str) -> str:
        window_length = len(s)
        j = 0

        while window_length >= 1:
            j = 0
            while j + window_length <= len(s):
                if self.isPalindrome(s[j:j+window_length]):
                    return s[j:j+window_length]
                j += 1
            
            window_length -= 1
