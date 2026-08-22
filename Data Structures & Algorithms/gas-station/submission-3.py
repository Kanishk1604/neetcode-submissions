class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): return -1
        totl_gas = 0
        res = 0
        for i in range(len(gas)):
            totl_gas += gas[i] - cost[i]
            if totl_gas < 0:
                totl_gas = 0
                res = i + 1

        return res