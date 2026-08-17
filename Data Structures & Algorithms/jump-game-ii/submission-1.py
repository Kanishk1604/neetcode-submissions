class Solution:
    def jump(self, nums: List[int]) -> int:
        #hashmap {index: jumps to reach last posi}
        #start from back 
        #[2,4,1,1,1,1]
        #{4: 1} {3:2} {2:3} {1:1}
        # if i + nums[i] in map 
        #then map[i] = map[i + nums[i]] + 1
        n = len(nums)
        jumpMap = {i: float("inf") for i in range(n)}
        jumpMap[n -1] = 0

        for i in range(n - 2, -1, -1):
            if nums[i] != 0:
                for j in range(1,nums[i] + 1):
                    if (j + i) < n:
                        jumpMap[i] = min(jumpMap[i], jumpMap[j+i] + 1)
        
        return jumpMap[0]