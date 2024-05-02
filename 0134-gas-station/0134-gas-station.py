class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        start_index=0
        current_gas=0
        for i in range(len(gas)):
            current_gas+=gas[i]-cost[i]
            if current_gas<0:
                current_gas=0
                start_index=i+1
        return start_index