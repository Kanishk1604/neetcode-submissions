class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
                #[]
            #[2]    []
        #[2,2]  [2]     [5]         []  
#[2,2,2] [2,2] [2,5] [2] [5,5] [5]  [6] []
#[2,2,2,2] [2,2,2]  [2,2,5] [2,2] [2,7]      
        subset = []
        res = []
        def dfs(i):
            if i >= len(nums) or sum(subset) > target:
                return 
            if sum(subset) == target:
                res.append(subset.copy())
                return 
            
            subset.append(nums[i])
            dfs(i)
            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return res
            
