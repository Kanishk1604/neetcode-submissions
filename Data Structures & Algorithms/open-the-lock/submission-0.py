class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == "0000":
            return 0

        q = deque(["0000"])

        visited = set()
        dead = set(deadends)
        if "0000" in dead:
            return -1
        res = 0
        while q:
            for i in range(len(q)):
                lock = q.popleft()
                if lock == target:
                    return res 
                # visited.add(lock)
                for j in range(4):
                    next_lock = ""
                    back_lock = ""
                    next_lock = lock[:j] + str((int(lock[j]) + 1) % 10) + lock[j + 1:]
                    back_lock = lock[:j] + str((int(lock[j]) - 1) % 10) + lock[j + 1:]
                    if next_lock not in dead and next_lock not in visited:
                        visited.add(next_lock)
                        q.append(next_lock)
                    if back_lock not in dead and back_lock not in visited:
                        visited.add(back_lock)
                        q.append(back_lock)
            res += 1
            
        
        return -1
                
                