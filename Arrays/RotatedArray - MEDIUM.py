# https://leetcode.com/problems/rotate-array/
# my solution
class Solution(object):
    def rotate(self, nums, k):
        k = k % len(nums)
        lp = 0
        rp = len(nums)-1
        while lp < rp:
            nums[lp], nums[rp] = nums[rp], nums[lp]
            lp+=1
            rp-=1
        lp = 0
        rp = k-1
        while lp < rp:
            nums[lp], nums[rp] = nums[rp], nums[lp]
            lp+=1
            rp-=1
        lp = k
        rp = len(nums)-1
        while lp < rp:
            nums[lp], nums[rp] = nums[rp], nums[lp]
            lp+=1
            rp-=1
# lc solution
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])