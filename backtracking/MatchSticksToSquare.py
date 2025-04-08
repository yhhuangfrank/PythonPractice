from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0: return False
        target = total // 4
        matchsticks.sort(reverse=True)
        sides = [0] * 4

        def backtracking(i):
            if i == len(matchsticks): return True
            for j in range(4):
                if sides[j] + matchsticks[i] > target: continue
                sides[j] += matchsticks[i]
                if backtracking(i + 1): return True
                sides[j] -= matchsticks[i]
            return False
        
        return backtracking(0)
    

sol = Solution()
print(sol.makesquare([1,1,2,2,2]))
print(sol.makesquare([3,3,3,3,4]))
print(sol.makesquare([1,5,5,1,1,5,6]))