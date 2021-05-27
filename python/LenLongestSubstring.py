'''
Given a string s, find the length of the longest substring without repeating characters.

https://leetcode.com/problems/longest-substring-without-repeating-characters/ 
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: 
        def testLimits() -> None:
            nonlocal max_end
            nonlocal max_start
            nonlocal current_end
            nonlocal current_start

            if (max_end - max_start) < (current_end - current_start):
                    max_end = current_end
                    max_start = current_start
        
        max_start = 0
        max_end = 0
        current_start = 0
        current_end = 0
        map = {}
        for c in s:
            if c in map and current_start <= map[c]:
                testLimits()         
                current_start = map[c] + 1
            
            map[c] = current_end
            current_end += 1

        testLimits()
        return max_end - max_start


