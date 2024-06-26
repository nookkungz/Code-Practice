class Solution:
    def missingNumber(self, n, arr):
        num_set = set(arr) # <<< เปลี่ยนมาใช้ Set ทำให้โค้ดเร็วขึ้น
        for i in range(1, n + 1):
            if i not in num_set:
                return i
solution = Solution() 
n = 10
arr = [1,2,3,4,5,6,7,8,10]
print(solution.missingNumber(n , arr))