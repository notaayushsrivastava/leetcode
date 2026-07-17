class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substring = ''
        iter_substr = ''
        for i in s:
            if i not in iter_substr:
                iter_substr+=i
            else: 
                iter_substr = i
            if len(iter_substr)>len(longest_substring):
                longest_substring = iter_substr
        
        return len(longest_substring)