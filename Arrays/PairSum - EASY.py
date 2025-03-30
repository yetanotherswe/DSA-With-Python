# https://www.naukri.com/code360/problems/pair-sum_697295?leftPanelTabValue=PROBLEM

from os import *
from sys import *
from collections import *
from math import *
def pairSum(arr, S):
    arr.sort()  # Sorting the array (O(N log N))
    left, right = 0, len(arr) - 1
    result = []

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == S:
            result.append((arr[left], arr[right]))  # Store the valid pair

            # Move left and right pointers while handling duplicates
            left += 1
            right -= 1  # Reduce right to check more pairs
        
        elif current_sum < S:
            left += 1  # Increase sum by moving left
        
        else:
            right -= 1  # Decrease sum by moving right

    return sorted(result)  # Sort pairs for correct output order
