'''
Given an integer n represented as a string, return the smallest good base of n.
We call k >= 2 a good base of n, if all digits of n base k are 1's.

https://leetcode.com/problems/smallest-good-base/
'''

from math import log

class Solution:
    def smallestGoodBase(self, n: str) -> str:
        n_int = int(n)

        max_digits = int(log(n_int, 2))
        min_digits = 1

        for k in range(max_digits, min_digits, -1):
            # From the problem definition
            # n = 1 + b + b^2 + ... + b^k [1] =>
            # n = (b^(k + 1) - 1) / (b - 1) [2]
            
            # From binomial theorem
            # (1 + b) ^ k = sum[binom(k, i) * b ^ i], since binom(k, i) >= 1 =>
            # n < (1 + b) ^ k [3] and, from [1],
            # n > b ^ k [4], thefore we just need to test:
            base = int(n_int ** k ** -1)

            # From [2]
            if n_int == (base ** (k + 1) - 1) // (base - 1):
                return str(base)

        # For k = 1, above loop breaks because n = 1 + b and [3] does not hold
        return str(n_int - 1)
        