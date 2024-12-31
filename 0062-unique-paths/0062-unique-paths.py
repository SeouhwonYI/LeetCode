class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        a, b = min(m-1,n-1), max(m-1,n-1)
        sol = 1
        for i in range(a):
            sol *= (a+b-i)
            sol /= (i+1)
        return int(sol)