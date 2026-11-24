class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        
        operator = set("+-*/")
        st=[]
        for i in tokens:
            if i not in operator:
                st.append(i)
            else:
                op2=int(st.pop())
                op1=int(st.pop())
                if i=='+':
                    st.append(op1+op2)
                elif i=='-':
                    st.append(op1-op2)
                elif i=='*':
                    st.append(op1*op2)
                else:
                    st.append(int(op1/op2))
        return int(st[-1])

