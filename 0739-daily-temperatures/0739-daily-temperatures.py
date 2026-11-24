class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n=len(temperatures)
        days=[0]*n
        stack=[]
        for i in range(n):
            curr=temperatures[i]
            while(stack):
                idx=stack[-1]
                top=temperatures[idx]
                if (top<curr):
                    days[idx]=i-idx 
                    stack.pop()
                else:
                    break
            stack.append(i)
        return days 
