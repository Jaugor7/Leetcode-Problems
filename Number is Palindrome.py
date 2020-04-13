https://leetcode.com/problems/palindrome-number/submissions/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        res , xcopy= 0, x
        while x > 0:
            res = res*10 + x%10
            x //= 10
        if res == xcopy:
            return True
        else:
            return False
        