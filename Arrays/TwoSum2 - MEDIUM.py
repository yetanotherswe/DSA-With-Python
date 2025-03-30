# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

class Solution(object):
    def twoSum(self, numbers, target):
        leftPointer = 0
        rightPointer = len(numbers) - 1
        while leftPointer < rightPointer:
            curr_sum = numbers[leftPointer]+numbers[rightPointer]
            if curr_sum == target:
                return [leftPointer+1,rightPointer+1]
            elif curr_sum < target:
                leftPointer += 1
            else:
                rightPointer -= 1