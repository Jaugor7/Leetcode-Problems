https://leetcode.com/problems/longest-common-prefix/submissions/


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        res = ''
        if n == 0:
            return res
        minlen = len(strs[0])
        index = 0
        for i in range(1,len(strs)):
            if len(strs[i]) < minlen:
                index = i
                minlen = len(strs[i])
            
        for i in range(len(strs[index])):
            flag = 0
            f2 = 0
            for j in range(n):
                if strs[0][i] == strs[j][i]:
                    flag += 1
                else:
                    f2 = 1
            if flag == n:
                res += strs[0][i]
            if f2 == 1:
                break
        return res
                    
                
        