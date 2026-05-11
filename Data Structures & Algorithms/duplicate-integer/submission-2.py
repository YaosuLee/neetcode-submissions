class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for x in nums:
            # 1. Kiểm tra: x đã có TRONG (in) seen chưa?
            if x in seen: 
                return True
            # 2. Nếu chưa, hãy THÊM x vào seen để ghi nhớ
            seen.add(x)
        return False