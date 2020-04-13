https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:    
        start, end , ml= 0, 1, 1
        sub = ''
        if s == '':
            return 0
        sl = len(s)
        if sl == len(set(s)):
            return sl
        
        for i in range(sl):
            for j in range(i+1,sl+1):
                substr = set(s[i:j])
                nl = len(substr)
                if nl == j-i:
                    if nl > ml:
                        ml = nl
                else:
                    break
        return ml