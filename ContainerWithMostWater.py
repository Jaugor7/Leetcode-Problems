https://leetcode.com/problems/container-with-most-water/submissions/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = len(height)
        if l == 0:
            return 0
        if l == 1:
            return height[0]
        maxv = 0 
        j, i = l-1, 0
        while i < j:
            vol = min(height[i],height[j])* (j-i)
            if  vol > maxv:
                maxv = vol
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return maxv