https://leetcode.com/problems/3sum/submissions/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        out = set()
        if l < 3:
            return []
        nums.sort()
        if nums[0]+nums[1]+nums[2] > 0 or nums[-1]+nums[-2]+nums[-3] < 0:
            return []
        for i in range(l-2):
            if nums[i]+nums[i+1]+nums[i+2] > 0 or nums[i]+nums[-1]+nums[-2] < 0:
                continue
            lptr, rptr = i+1,l-1
            while lptr < rptr:
                s = nums[i]+nums[lptr]+nums[rptr]
                if s == 0:
                    temp = (nums[i],nums[lptr],nums[rptr])
                    out.add(temp)
                    lptr += 1
                    rptr -= 1
                elif s > 0:
                    rptr -= 1
                elif s < 0:
                    lptr += 1
                    
        return list(out)