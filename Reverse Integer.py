https://leetcode.com/problems/reverse-integer/submissions/


class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        flag = 0

        if x < 0:
            flag = 1
            x = x * -1
            
        if x > 2147483647:
            return 0   
        
        while x > 0:
            rev = rev * 10 + x % 10
            x //= 10
            
        if rev > 2147483647:
            return 0
        
        if flag == 1:
            return rev * -1
        else:
            return rev 