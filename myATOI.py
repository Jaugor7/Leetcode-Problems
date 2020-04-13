https://leetcode.com/problems/string-to-integer-atoi/submissions/


class Solution:
    def myAtoi(self, st: str) -> int:
        st = st.strip()
        
        if len(st) == 0:
            return 0
        
        output, sign,  = 0,1

        if st[0] == '-':
            sign = -1
            st = st[1:]
            
        elif st[0] == '+':
            st = st[1:]
            
        if len(st) == 0:
            return 0
        if  st[0].isdigit() == False:
            return 0
        for i in range(len(st)):
            if st[i].isdigit():
                output = output*10 + int(st[i])
            else:
                break

        output = sign*output
        if output < -2**31:
            return -2**31
        elif output > 2**31 - 1:
            return 2**31 -1
        return output
        