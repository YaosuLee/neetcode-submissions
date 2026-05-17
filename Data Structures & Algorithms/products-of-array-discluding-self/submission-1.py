import numpy as np
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lenght = len(nums)
        output = [0]*lenght
        l = [1]*lenght
        r = [1]*lenght
        for i in range(1, lenght):
            l[i] = nums[i-1] * l[i-1] 
            r[-i-1] = nums[-i] * r[-i] 
        output = list(map(lambda x, y: x * y, l, r))
        return output