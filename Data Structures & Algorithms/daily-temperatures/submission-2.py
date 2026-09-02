class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # monotonic stack, descending
        stack = []
        ans = [0]*len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                # warmer
                old_t, old_i = stack.pop()
                ans[old_i] = i - old_i
            stack.append((t, i))
        
        return ans

        