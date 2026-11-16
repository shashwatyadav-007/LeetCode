class Solution:
    def maxArea(self, height: list[int]) -> int:
        l=0
        n=len(height)
        r=n-1
        maxi=0
        while l < r:
            maxi=max(maxi,((r-l)*min(height[r],height[l])))
            if height[r]>height[l]:
                l+=1
            else:
                r-=1
        return maxi