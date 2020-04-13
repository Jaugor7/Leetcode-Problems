class Solution(object):
    def fourSum(self, nums, target):
        length = len(nums)
        if length < 4:
            return []
        nums.sort()
        ret = []
        if nums[0]+nums[1]+nums[2]+nums[3]>target or nums[-4]+nums[-3]+nums[-2]+nums[-1] < target:
            return []
        for i in range(length-3):
            if nums[i]+nums[-1]+nums[-2]+nums[-3] < target or nums[i]+nums[i+1]+nums[i+2]+nums[i+3] > target:
                continue
            for j in range(i+1, length-2):
                if nums[i]+nums[j]+nums[-1]+nums[-2] < target or nums[i]+nums[j]+nums[j+1]+nums[j+2] > target:
                    continue            
                left, right = j+1, length-1
                remain = target - nums[i] - nums[j]
                while left < right:
                    sums = nums[left]+nums[right]
                    if sums == remain:
                        temp = [nums[i], nums[j], nums[left], nums[right]]
                        if temp not in ret:
                            ret.append(temp)
                        left += 1
                        right -= 1
                    elif sums < remain:
                        left += 1
                    else:
                        right -= 1
        return ret
