class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a = {}
        out = 0
        for i, x in enumerate(numbers):
            out = target - x
            if out in a:
                return [a[out]+1, i+1]
            
            a[x] = i
            