# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/
class Solution(object):
    def check(self, nums):
        count = 0
        if len(nums) in [0,1,2]:
            return True
        checkPoint = float('-inf')
        for i in range(1,len(nums)):
            if nums[i] >= nums[i-1]:
                continue
            else:
                count += 1
                if count > 1:
                    return False
                checkPoint = nums[i]
        if count > 0:
            if nums[0] >= nums[len(nums)-1]:
                return True
            else:
                return False
        else:
            if nums[0] > nums[len(nums)-1]:
                return False
            else:
                return True

        