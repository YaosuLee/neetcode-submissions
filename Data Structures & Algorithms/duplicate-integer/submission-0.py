class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        c = []
        for x in nums:
            if x in c:
                return True
            c.append(x)
        return False