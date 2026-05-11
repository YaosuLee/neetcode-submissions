class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # char_s = set(s)
        # char_t = set(t)
        count = {}
        if len(s) != len(t):
            return False
        for i in s:
            count[i] = count.get(i,0) + 1
        for j in t:
            if j in count:
                count[j] = count[j] - 1
                if count[j] < 0:
                    return False
            else:
                return False            
        return True
