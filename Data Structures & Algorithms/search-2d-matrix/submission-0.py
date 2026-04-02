class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def _bin_search(matrix, target, cond_found, cond_high):
            # Step 1: find correct row
            lo, hi = 0, len(matrix) - 1

            while lo <= hi: 
                mid = (hi - lo) // 2 + lo
                if cond_found(matrix, target, mid):
                    return mid
                if cond_high(matrix, target, mid):
                    lo = mid + 1
                else: 
                    hi = mid - 1

            return -1

        # Row conditions
        cond_found = lambda _matrix, _target, _mid: _matrix[_mid][0] <= _target <= _matrix[_mid][-1]
        cond_high = lambda _matrix, _target, _mid: _target > _matrix[_mid][-1]

        row = _bin_search(
            matrix, 
            target,
            cond_found, 
            cond_high
        )
        if row == -1: 
            return False

        # Step 2: find column (value in correct row)

        cond_found = lambda _row, _target, _mid: _row[_mid] == target
        cond_high = lambda _row, _target, _mid: _target > _row[_mid]

        col = _bin_search(
            matrix[row],
            target, 
            cond_found, 
            cond_high
        )

        if col == -1: 
            return False

        return True

