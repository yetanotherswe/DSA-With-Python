# leetcode.com/problems/remove-duplicates-from-sorted-array
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 1
        k = 0
        l = 0
        for l in range(0,len(nums)-1):
            if nums[l] != nums[l+1]:
                nums[k] = nums[l]
                k += 1
        nums[k] = nums[l+1]
        return k+1
        