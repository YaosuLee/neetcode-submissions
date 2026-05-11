from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ts = defaultdict(list) # Tự động tạo [] nếu key chưa có
        for x in strs:
            key = "".join(sorted(x))
            ts[key].append(x)
        return list(ts.values())

                
            
        
