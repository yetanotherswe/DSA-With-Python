# https://leetcode.com/problems/3sum

class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        new_nums = []
        n = len(nums)

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicate elements for i
                continue
            if nums[i] > 0:  # Since nums is sorted, further numbers will also be > 0
                break

            leftPointer, rightPointer = i + 1, n - 1

            while leftPointer < rightPointer:
                curr_sum = nums[i] + nums[leftPointer] + nums[rightPointer]

                if curr_sum == 0:
                    new_nums.append([nums[i], nums[leftPointer], nums[rightPointer]])

                    # Move both pointers and avoid duplicates
                    leftPointer += 1
                    rightPointer -= 1

                    while leftPointer < rightPointer and nums[leftPointer] == nums[leftPointer - 1]:
                        leftPointer += 1  # Skip duplicate left values
                    
                    while leftPointer < rightPointer and nums[rightPointer] == nums[rightPointer + 1]:
                        rightPointer -= 1  # Skip duplicate right values

                elif curr_sum < 0:
                    leftPointer += 1  # Increase sum by moving left pointer
                else:
                    rightPointer -= 1  # Decrease sum by moving right pointer

        return new_nums
