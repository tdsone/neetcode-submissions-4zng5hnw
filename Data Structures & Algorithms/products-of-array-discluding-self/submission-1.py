"""
Key insight

product[i] = product(nums[0:i]) * product(nums[i+1:])
product[i] = prefix[i] * suffix[i]

now we can just compute: 
prefix[i]: product from 0 to i-1
suffix[i]: product from i+1 to end

Edge cases: 
prefix[0] = 1
suffix[-1] = 1
suffix[-2] = nums[-1] oder mit j = N - 1 - iund i = 1, suffix[j] = suffix[j + 1] * nums[j + 1]
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        pfx_prod = [1] * N 
        sfx_prod = [1] * N

        for i in range(1, N):
            pfx_prod[i] = pfx_prod[i - 1] * nums[i - 1]
            j = N - 1 - i # j = N - 1 - 1 = N - 2
            sfx_prod[j] = sfx_prod[j + 1] * nums[j + 1]

        res = [1] * N
        for i in range(N):
            res[i] = pfx_prod[i] * sfx_prod[i]

        return res








