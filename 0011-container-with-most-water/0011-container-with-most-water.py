class Solution:
    def maxArea(self, height: list[int]) -> int:
        l=0
        n=len(height)
        r=n-1
        maxi=0
        while l < r:
            min_height=min(height[r],height[l])
            area=((r-l)*min_height)
            if area>maxi:
                maxi=area
            if height[r]>height[l]:
                l+=1
            else:
                r-=1
        return maxi