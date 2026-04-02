class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        """
        Time: nlogm 

        Lower bound:
        - math.ceil(sum(piles) / h)
        Upper bound:
        - max(piles)

        Binary search through k with evaluate(k)

        

        Option 2:
        wasted = sum([k - pile % k for pile in piles])
        -> find argmin_k(wasted)

        d wasted / d k 
        - gradient of k - pile % k wrt k = 1 + floor(pile / k)
        """
        def count_hours(k):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
            return hours

        # binary search over k

        lo, hi = math.ceil(sum(piles) / h), max(piles)
        print(lo, hi)

        best_k = max(piles)
        while lo <= hi:
            mid = (lo + hi) // 2
            if count_hours(mid) == h:
                hi = mid - 1
                best_k = min(best_k, mid)
            elif count_hours(mid) > h: # k is too low
                lo = mid + 1
            elif count_hours(mid) < h: # k might be too high
                hi = mid - 1
                best_k = min(best_k, mid)

        return best_k

