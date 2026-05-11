class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = []
        b = {}
        for x in strs:
            key = "".join(sorted(x))
            if key in b:
                b[key].append(x)
            else:
                b[key] = [x]
        return list(b.values())

                
            
        
