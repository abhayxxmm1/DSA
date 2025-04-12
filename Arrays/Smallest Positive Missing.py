'''
You are given an integer array arr[]. Your task is to find the smallest positive number missing from the array.

Note: Positive number starts from 1. The array can have negative integers too.

Examples:

Input: arr[] = [2, -3, 4, 1, 1, 7]
Output: 3
Explanation: Smallest positive missing number is 3.
Input: arr[] = [5, 3, 2, 5, 1]
Output: 4
Explanation: Smallest positive missing number is 4.
Input: arr[] = [-8, 0, -1, -4, -3]
Output: 1
Explanation: Smallest positive missing number is 1.
Constraints:  
1 <= arr.size() <= 105
-106 <= arr[i] <= 106
'''
class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr):
        n = len(arr)
        for i in range(n):
            
            while 1 <= arr[i] <=n and arr[i] != arr[arr[i]-1]:
                
                temp = arr[i]
                arr[i] = arr[arr[i]-1]
                arr[temp - 1] = temp
                
        for i in range(1,n+1):
            if i != arr[i - 1]:
                return i
                
        return n+1
