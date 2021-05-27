'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false

https://leetcode.com/problems/valid-anagram/
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        def getCharCount(s: str) -> dict:
            char_count = {}
            for c in s:
                if c in char_count:
                    char_count[c] += 1
                else:
                    char_count[c] = 1 
            
            return char_count
        
        count_s = getCharCount(s)
        count_t = getCharCount(t)

        if len(count_t) != len(count_s):
            return False
            
        for key_s, value_s in count_s.items():    
            if key_s not in count_t:
                return False
            
            if count_t[key_s] != value_s:
                return False

        return True



