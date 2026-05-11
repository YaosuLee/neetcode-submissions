class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = {}
        b = []
        nums = sorted(nums)
        for i in nums:
            if i in a:
                a[i] += 1
            else:
                a[i] = 1
        li = sorted(a.items(), key=lambda item: item[1], reverse=True)
        for x in li[:k]:
            b.append(x[0])
        return b
