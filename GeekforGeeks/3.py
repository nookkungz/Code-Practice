class Solution:
    def valueEqualToIndex(self,arr, n):
        answ = []
        for i in range(n):
            if arr[i] == i+1:
                answ.append(i+1)
        return answ
	
solution = Solution() 
n = 3
arr = [1,2,3]
print(solution.valueEqualToIndex(arr , n))