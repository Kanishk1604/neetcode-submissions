class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
                #[]
            #[2]    []
        #[2,2]  [2]     [5]         []  
#[2,2,2] [2,2] [2,5] [2] [5,5] [5]  [6] []
#[2,2,2,2] [2,2,2]  [2,2,5] [2,2] [2,7]      
        subset = []
        res = []
        def dfs(i, total):
            if i >= len(nums) or total > target:
                return 
            if total == target:
                res.append(subset.copy())
                return 
            
            subset.append(nums[i])
            dfs(i, total + nums[i])
            subset.pop()
            dfs(i + 1, total)
        
        dfs(0, 0)
        return res
            
