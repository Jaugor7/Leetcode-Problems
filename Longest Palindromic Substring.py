https://leetcode.com/problems/longest-palindromic-substring/submissions/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        ml = 0
        sub = ''
        sl = len(s)
        
        if s == '' or sl == 1:  # Empty Input String or Single Char String
            return s
        ls = len(set(s))
        
        if ls == 1 and sl > 1:  #All elements are same
            return s
        
        if sl == ls:
            return s[0]
        
        for i in range(sl):
            for j in range(i+1,sl+1):
                substr = s[i:j]
                
                if substr == substr[::-1]:
                    nl = len(substr)
                    if nl > ml:
                        ml = nl
                        sub=substr
        return sub