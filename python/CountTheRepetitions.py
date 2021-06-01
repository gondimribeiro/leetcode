'''
We define str = [s, n] as the string str which consists of the string s concatenated n times.

For example, str == ["abc", 3] =="abcabcabc".
We define that string s1 can be obtained from string s2 if we can remove some characters from 
s2 such that it becomes s1.

For example, s1 = "abc" can be obtained from s2 = "abdbec" based on our definition by removing 
the bolded underlined characters. You are given two strings s1 and s2 and two integers n1 and n2. 
You have the two strings str1 = [s1, n1] and str2 = [s2, n2].

Return the maximum integer m such that str = [str2, m] can be obtained from str1.

https://leetcode.com/problems/count-the-repetitions/
'''

class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        
        # Store (`rep1`, `rep2`) for a `idx1` of `s1` when finishing a search for `s2`.
        last_idx1 = {} 
        
        # Init variables
        len1, len2 = len(s1), len(s2)
        idx1, idx2 = 0, 0
        rep1, rep2 = 1, 0

        while rep1 <= n1:
            if s1[idx1] == s2[idx2]:
                idx2 += 1

                if idx2 == len2:
                    rep2 += 1
                    idx2 = 0

                    # When we finish searching an occurrence for `s2`, we check where we 
                    # are in `s1`. If we have seen this pattern before, we simply 
                    # compute the number of occurrences of `s1` and `s2` up to `n1` 
                    # repetitions.
                    if idx1 not in last_idx1:
                        last_idx1[idx1] = (rep1, rep2)
                    else:
                        last_rep1, last_rep2 = last_idx1[idx1]    

                        # Period of repetitions    
                        period_rep1 = rep1 - last_rep1
                        period_rep2 = rep2 - last_rep2

                        # Max number of `s1` repetitions of pattern and how many repetitions
                        # will be needed to reach `n1` after cloning this pattern
                        max_rep1 = (n1 - last_rep1) // period_rep1
                        remain_rep1 = (n1 - last_rep1) % period_rep1

                        # Update repetions
                        rep1 = n1 - remain_rep1
                        
                        # Time s2 will be found
                        max_rep2 = max_rep1 * period_rep2
                        rep2 = last_rep2 + max_rep2

            idx1 += 1
            if idx1 == len1:
                rep1 += 1
                idx1 = 0

        # divide c2 by n2 to get the result
        return rep2 // n2