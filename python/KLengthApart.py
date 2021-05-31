'''
Given an array nums of 0s and 1s and an integer k, return True if all 
1's are at least k places away from each other, otherwise return False.

https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/
'''
from typing import List

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        
        if 1 not in nums or k == 0:
            return True

        n = len(nums)
        dist = k
        for i in range(n): 
            if nums[i]:
                if dist < k:
                    return False
                dist = 0
            else: 
                dist += 1
            
        return True
            
