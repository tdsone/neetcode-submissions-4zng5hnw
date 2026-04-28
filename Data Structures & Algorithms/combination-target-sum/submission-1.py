class RevTree: 
    def __init__(self, val, up):
        self.val = val
        self.up = up
    
    def backtrack(self) -> list[int]:
        print()
        print("Backtracking")
        res = []
        curr = self
        prev = curr.val
        while curr:
            if not (curr.val - prev) == 0: res.append(curr.val - prev)
            print(f"{prev=}, {curr.val=}, {res=}")
            prev = curr.val
            curr = curr.up

        return res

class Solution:
    
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        """

        res = []
        nums_set = set(nums)
        root = RevTree(target, None)
        q = deque([root]) # (target, last subtractor)

        while q:
            curr = q.popleft()
            last_change = -1
            if curr.up:
                last_change = curr.up.val - curr.val 

            for n in nums:
                if not n >= last_change:
                    continue
                if curr.val - n < 0: 
                    continue
                if curr.val - n == 0:
                    res.append(RevTree(val=0, up=curr).backtrack())
                    continue
                
                q.append(RevTree(val=curr.val - n, up=curr))

        return res