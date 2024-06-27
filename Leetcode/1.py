class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lists = []
        for i in range (len(nums)):
            for j in (len(nums)):
                if nums[i] + nums[j] == target :
                    lists.append(nums[i],nums[j])
        return lists    
solution = Solution() 
nums = 2,7,11,15
target = 9
print(solution.twoSum(nums , target))