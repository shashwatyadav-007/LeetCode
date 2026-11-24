class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        
        operator = set("+-*/")
        st=[]
        for i in tokens:
            if i not in operator:
                st.append(int(i))
            else:
                op2=st.pop()
                op1=st.pop()
                if i=='+':
                    st.append(op1+op2)
                elif i=='-':
                    st.append(op1-op2)
                elif i=='*':
                    st.append(op1*op2)
                else:
                    st.append(int(op1/op2))
        return st[-1]

