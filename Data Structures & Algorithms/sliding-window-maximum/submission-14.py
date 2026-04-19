class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Deque solution
        """

        res = []
        q = deque()
        l = r = 0

        while r < len(nums):
            # 1. Remove elements from queue from right 
            # side that are smaller than nums[r] since
            # r will always be larger
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            q.append(r)

            # 2. if topmost element is out of window, remove it
            if q[0] < l:
                q.popleft()

            # 3. once we have a "full" window, return max
            if (r + 1) >= k: 
                res.append(nums[q[0]])
                # shift left pointer
                l += 1
            
            r += 1 

        return res
