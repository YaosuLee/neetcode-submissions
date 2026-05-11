class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        c = set()
        for x in nums:
            if x in c:
                return True
            c.add(x)
        return False