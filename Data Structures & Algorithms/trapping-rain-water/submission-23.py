class Solution:
    def trap(self, height: List[int]) -> int:
        """
        
        """
        print(f"{len(height)=}")
        trapped = [] 

        def _find_left_boundary(i):
            if i - 1 >= 0:
                return max(height[:i])                 
            return -1
        
        def _find_right_boundary(i):
            if i + 1 < len(height):
                return max(height[i+1:])                 
            return -1

        for i in range(len(height)):
            lh = _find_left_boundary(i)
            lr = _find_right_boundary(i)
            print(f"{i=}, {lh=}, {lr=}")
            if lr >= 0 and lh >= 0 and min(lh, lr) - height[i] >= 0:
                trapped.append(min(lh, lr) - height[i])
            else:
                trapped.append(0)

        print(trapped)

        return sum(trapped)



    