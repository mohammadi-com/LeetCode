class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = new_length = l = r = new_l = 0
        characters_dictionary = {}

        while r < len(s):
            if s[r] in characters_dictionary:
                new_l = characters_dictionary[s[r]] + 1
                for i in range(l, new_l):
                    characters_dictionary.pop(s[i])
                l = new_l
            else:
                new_length = r - l + 1
                if new_length > max_length:
                    max_length = new_length
            
            characters_dictionary[s[r]] = r
            r += 1
        
        return max_length
