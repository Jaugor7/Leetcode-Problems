https://leetcode.com/problems/median-of-two-sorted-arrays/submissions/


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i, j, flagi, flagj, lnum1, lnum2 = 0, 0, 0, 0, len(nums1), len(nums2)
        res = []
        
        if lnum1 == 0:
            flagi = 1
        if lnum2 == 0:
            flagj = 1 
            
        while i < lnum1 and j < lnum2:
            if nums1[i] <= nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1
                           
            if i == lnum1:
                flagi = 1
            if j == lnum2:
                flagj = 1
        
        if flagi == 1:
            while j < lnum2:
                res.append(nums2[j])
                j += 1
        if flagj == 1:
            while i < lnum1:
                res.append(nums1[i])
                i += 1
                            
        l = lnum1 + lnum2
        if l%2 == 0:
            return (res[l//2]+res[(l//2)-1])/2
        else:
            return res[l//2]
        