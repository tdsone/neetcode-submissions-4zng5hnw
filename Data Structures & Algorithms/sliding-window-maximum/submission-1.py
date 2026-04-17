class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Goal: O(nlogn) time and O(n) size

        Naive solution:
        - call max on each shift -> O(k*(n - k))
        """

        l, r = 0, k - 1
        result = [] 
        
        while r < len(nums):
            result.append(max(nums[l : r + 1]))
            r += 1
            l += 1

        return result