class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        start = set(nums)
        print(nums)
        max_count = 0
        for x in nums:
            if x - 1 not in nums:
                y = x + 1
                while y in nums:
                    y+=1
                max_count = max(max_count, y-x)  
        return max_count
