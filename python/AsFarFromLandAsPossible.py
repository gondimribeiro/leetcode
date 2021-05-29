'''
Given an n x n grid containing only values 0 and 1, where 0 represents water 
and 1 represents land, find a water cell such that its distance to the 
nearest land cell is maximized, and return the distance. If no land or water
exists in the grid, return -1.

The distance used in this problem is the Manhattan distance: the distance 
between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

https://leetcode.com/problems/as-far-from-land-as-possible/
'''
from typing import List, Tuple
from collections import deque

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:    
        
        # Init BFS
        n = len(grid)
        queue = deque()
        distance = [[-1] * n for i in range(n)]       
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    queue.append((i, j))
                    distance[i][j] = 0
                
        # BFS
        max_dist = -1
        deltas = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        while queue:
            i, j, = queue.popleft()
            for d in deltas:
                next_i, next_j = i + d[0], j + d[1]
                if 0 <= next_i < n and 0 <= next_j < n and \
                    distance[next_i][next_j] == -1:
                    
                    curr_dist = distance[i][j] + 1
                    distance[next_i][next_j] = curr_dist
                    queue.append((next_i, next_j))

                    max_dist = max_dist if max_dist > curr_dist else curr_dist
        
        return max_dist
