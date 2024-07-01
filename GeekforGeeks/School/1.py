class Solution:
    def seriesSum(self, n: int) -> int:
        total = 0
        for i in range(1, n + 1):
            total += i
        return total
solution = Solution() 
print(solution.seriesSum(5))