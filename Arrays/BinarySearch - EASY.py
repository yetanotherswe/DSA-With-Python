#User function Template for python3

class Solution:
    ##Complete this function
    def searchInSorted(self,arr, k):
        n = len(arr)/2
        st = 0
        end = len(arr) - 1
        while st<=end:
            mid = int((st+end)/2)
            if arr[mid] == k:
                return True
            if arr[mid] > k:
                end = mid - 1
            else:
                st = mid + 1
        return False
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        A = [int(x) for x in input().strip().split()]
        k = int(input())
        ob = Solution()
        print("true" if ob.searchInSorted(A, k) else "false")
        print("~")

# } Driver Code Ends