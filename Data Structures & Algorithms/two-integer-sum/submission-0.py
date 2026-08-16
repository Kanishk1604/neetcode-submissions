class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        res = []
        for i in range(len(nums)):
            if (target - nums[i]) in hashmap:
                res.append(hashmap[target - nums[i]])
                res.append(i)
                return res
            hashmap[nums[i]] = i
        
        return []