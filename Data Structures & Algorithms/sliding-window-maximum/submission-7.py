class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, 0
        q = deque()
        res = []
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            
            if r >= k - 1:
                res.append(nums[q[0]])
                if q and l == q[0]:
                    q.popleft()
                l += 1
            
            r += 1
        
        return res


            