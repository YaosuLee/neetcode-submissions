class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        out = {}
        for i, x in enumerate(nums):
            need = target - x
            if need in out:
                return [out[need],i]
            out[x] = i
            print(out)

