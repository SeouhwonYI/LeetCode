class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # m, n = len(grid), len(grid[0])
        # itr = m + n -2

        # for k in range(itr):
        #     # (0, k+1), (1, k), (2, k-1), ... , (k+1, 0)
        #     for i in range(k+2):
        #         j = (k+1) - i
        #         if (i < m and j < n):
        #             if (i == 0): up = 200 * itr + 1
        #             else: up = grid[i-1][j]
        #             if (j == 0): left = 200 * itr + 1
        #             else: left = grid[i][j-1]

        #             grid[i][j] = min(up, left) + grid[i][j]

        # return grid[m-1][n-1]

        m, n = len(grid), len(grid[0])
        
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]
        
        for i in range(1, n):
            grid[0][i] += grid[0][i-1]
        
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        
        return grid[-1][-1]