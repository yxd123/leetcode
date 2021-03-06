# -*- coding: utf-8 -*-

"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.
Example 1:
Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

Analysis:
This is a DP problem. Diffrent of uniquePaths, there contains some obstacles in path.

Notice boundary:
1. matrix[0][0~n] and matrix[0~m][0] must be init based on obstacleGrid

    if i == 0 or j == 0:
        if obstacleGrid[i][j] == 1 \
                or (matrix[i - 1][j] == 0 and i >= 1) \
                or (matrix[i][j - 1] == 0 and j >= 1):
            matrix[i][j] = 0
        else:
            matrix[i][j] = 1
2. if the end of grid is obstacle, return 0

Analysis:
1. DP solution, like unique-path.
2. Only init matrix[0][0].
3. Add rule:
            if obstacleGrid[i][j] == 1:
                    continue
"""


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0]) if m > 0 else 0
        # Init matrix
        matrix = [[0 for j in range(n)] for i in range(m)]
        # Init a start point
        matrix[0][0] = 1
        for i in range(1, m):
            # i == 0 means row 0
            reach_top = False if i == 0 else True
            for j in range(1, n):
                # If obstacleGrid contains (i, j) means no path
                if obstacleGrid[i][j] == 1:
                    continue
                # j == 0 means column 0
                reach_left = False if j == 0 else True
                if reach_left:
                    matrix[i][j] += matrix[i][j - 1]
                if reach_top:
                    matrix[i][j] += matrix[i - 1][j]
        return matrix[m-1][n-1]



if __name__ == '__main__':
    s = Solution()
    m1 = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    m2 = [[1]]
    m3 = [[1, 0]]
    m4 = [[0, 0], [0, 1]]
    print s.uniquePathsWithObstacles(m1)
    print s.uniquePathsWithObstacles(m2)
    print s.uniquePathsWithObstacles(m3)
    print s.uniquePathsWithObstacles(m4)
