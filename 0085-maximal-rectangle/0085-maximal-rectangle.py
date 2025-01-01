class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n_col = len(matrix[0])
        heights = [0] * (n_col + 1)
        max_area = 0

        for row in matrix:
            for i in range(n_col):
                # heights of i-th column up to row-th row
                heights[i] = heights[i] + 1 if row[i] == "1" else 0
            
            stack = [-1]
            for i in range(n_col+1):
                # 0 on left top position -> compute up to previous column box
                while heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i - stack[-1] - 1
                    max_area = max(max_area, h * w)

                stack.append(i)
        return max_area