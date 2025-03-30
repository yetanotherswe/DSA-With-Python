# https://www.geeksforgeeks.org/problems/second-largest3735/1

#User function Template for python3
class Solution:
    def getSecondLargest(self, arr):
        max = float('-inf')
        for i in arr:
            if i >= max:
                max = i
        max_2 = float('-inf')
        for i in arr:
            if i >= max_2 and i != max:
                max_2 = i
        if max_2 == float('-inf'):
            return -1
        return max_2


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSecondLargest(arr)
        print(ans)
        print("~")
# } Driver Code Ends