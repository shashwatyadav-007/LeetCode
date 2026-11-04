class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        pos=[]
        neg=[]
        for i in nums:
            if i>=0:
                pos.append(i)
            else:
                neg.append(i)
        for i in range(len(nums)//2):
            nums[i*2]=pos[i]
            nums[i*2+1]=neg[i]
        return nums