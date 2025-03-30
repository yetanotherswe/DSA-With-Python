# https://leetcode.com/problems/sum-of-unique-elements/description/

class Solution(object):
    def sumOfUnique(self, nums):
        elementsCount = {}
        sum = 0
        for item in nums:
            if item in elementsCount:
                elementsCount[item] += 1
            else:
                elementsCount[item] = 1
        for element in elementsCount:
            if elementsCount[element] == 1:
                sum += element
        return sum
        
        