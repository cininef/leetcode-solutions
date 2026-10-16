class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        def backtrack(sol, num_set):
            if len(sol) == len(nums):
                res.append(sol)
                return
            # all next states
            for i in nums:
                # legal states
                if i not in num_set:
                    cur = sol.copy() + [i]
                    num_set.add(i)
                    backtrack(cur, num_set)
                    num_set.remove(i)
        backtrack([], set())
        return res