class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        Observation: 
        -   the lower bar is limiting the volume and only 
            finding a higher lower bar will increase the volume
        -   

        Idea 1: start on the outside with two pointers
        - move inwards
        """

        def volume(l, r):
            return (r - l) * min(heights[l], heights[r])

        l, r = 0, len(heights) - 1
        max_vol = (len(heights) - 1) * min(heights[l], heights[r])

        while l < r:
            if heights[l] < heights[r]:
                while l < r and heights[l] < heights[r]:
                    l += 1
                    print("moving left pointer")
                    max_vol = max(max_vol, volume(l, r))
            elif heights[l] > heights[r]:
                while l < r and heights[l] > heights[r]:
                    r -= 1
                    max_vol = max(max_vol, volume(l, r))
                    print("moving right pointer")
            else:
                # Find closest improvement
                print("heights are equal")
                threshold = heights[l]
                l_init, r_init = l, r
                while l < r: 
                    print("l, r", l, r, "heights", heights[l], heights[r])
                    left_larger = heights[l] > threshold
                    right_larger = heights[r] > threshold
                    print("_larger", left_larger, right_larger)
                    if left_larger or right_larger:
                        # assign new l or r
                        l = l_init if heights[r] >= heights[l] else l
                        r = r_init if heights[r] < heights[l] else r
                        print("breaking")
                        break
                    else:
                        l += 1
                        r -= 1
            print(f"Updated pointers to l: {l}/{heights[l]} and r: {r}/{heights[r]}")
            
            max_vol = max(max_vol, (r - l) * min(heights[l], heights[r]))
            print("max_vol", max_vol)
            print()

        return max_vol