class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        l_max = 0
        r_max = 0
        out = 0
        while left <= right:
            if l_max <= r_max:
                l_max = max(l_max, height[left])
                out += l_max - height[left]
                left +=1
            else:
                r_max = max(r_max, height[right])
                out += r_max - height[right]
                right -=1
        return out

            
