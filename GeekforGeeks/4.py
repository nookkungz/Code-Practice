class Solution:
    def print2largest(self,arr, n):
        arr = sorted(arr)
        while arr[len(arr)-1] == arr[len(arr)-2] :
            arr.pop(len(arr)-1)
            if len(arr) == 1 :
                break  
        new = arr[len(arr)-2]
        if len(arr) == 1 :
            return -1
        return new
	
solution = Solution() 
n = 5
arr = [1,7,6,4,5]
print(solution.print2largest(arr , n))