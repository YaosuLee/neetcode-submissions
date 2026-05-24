class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        start = set()
        nums.sort()
        print(nums)
        max_count = 0
        count = 1
        if len(nums) == 1:
            return 1
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] == 1:
                count += 1
            elif nums[i+1] - nums[i] == 0:
                pass
            else:
                count = 1
            if count >= max_count:
                max_count = count
        return max_count

