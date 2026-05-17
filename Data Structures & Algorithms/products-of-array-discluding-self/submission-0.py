import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0]*len(nums)
        for i in range(len(nums)):
            temp = nums.copy()
            temp[i] = 1
            output[i] = math.prod(temp)
        return output