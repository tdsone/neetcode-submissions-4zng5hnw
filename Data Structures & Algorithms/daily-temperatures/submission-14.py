class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        result = [0] * len(temperatures)

        print(result)

        for i, t in enumerate(temperatures):
            if len(stack) == 0: 
                stack.append((t, i))
                continue

            while len(stack) > 0 and t > stack[-1][0]:
                val, idx = stack.pop()
                result[idx] = i - idx
            
            stack.append((t, i))

        return result



