from typing import List


class Solution:
    # 暴力解, O(n ^ 2) time
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for i, n in enumerate(gas):
            if n - cost[i] < 0:
                continue
            temp = (i + 1) % len(gas)
            curr = n - cost[i]
            complete = True
            while temp != i:
                curr = curr + gas[temp] - cost[temp]
                if curr < 0:
                    complete = False
                    break
                temp = (temp + 1) % len(gas)
            if complete:
                return i
        return -1

    # Greedy, O(n) time
    def canCompleteCircuitV2(self, gas: List[int], cost: List[int]) -> int:
        total_surplus = 0
        surplus = 0
        start = 0
        for i, n in enumerate(gas):
            surplus = surplus + n - cost[i]
            total_surplus = total_surplus + n - cost[i]
            if surplus < 0:
                surplus = 0
                start = i + 1
        if total_surplus < 0:
            return -1
        return start


sol = Solution()
gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
print(sol.canCompleteCircuit(gas, cost))
print(sol.canCompleteCircuitV2(gas, cost))


