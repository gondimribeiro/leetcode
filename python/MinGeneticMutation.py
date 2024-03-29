'''
A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from a gene string start to a gene string end where one mutation is defined as one single character changed in the gene string.

For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.

Given the two gene strings start and end and the gene bank bank, return the minimum number of mutations needed to mutate from start to end. If there is no such a mutation, return -1.

Note that the starting point is assumed to be valid, so it might not be included in the bank.

https://leetcode.com/problems/minimum-genetic-mutation/
'''

from typing import List
from collections import deque

class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        def isMutation(s: str, t: str) -> bool:
            has_diff = False
            for base_s, base_t in zip(s, t):
                if base_s != base_t:
                    if has_diff:
                        return False
                    else:
                        has_diff = True
            
            return has_diff

        # BFS
        # previous node, current node, number of mutations
        queue = deque([("", start, 0)]) 
        while queue:
            previous, current, num_mutations = queue.popleft()

            if current == end:
                return num_mutations
            
            for gene in bank:
                if gene != previous and isMutation(current, gene):
                    queue.append((current, gene, num_mutations + 1))
                                
        return -1
