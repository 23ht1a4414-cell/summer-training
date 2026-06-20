'''A retail company records daily sales. 
Given an array representing sales for N days and a target value K, find the length of the longest 
continuous period whose total sales equal K. 
If no such period exists, print -1. 
Input 
8 
3 1 2 4 2 1 1 3 
8 
Output 
4 
Explanation 
Subarray: 
1 2 4 1 
has sum 8 and length 4. 
Constraints 
1 ≤ N ≤ 10^5 -10^4 ≤ arr[i] ≤ 10^4'''
n = int(input())
arr = list(map(int, input().split()))
k = int(input())

prefix = 0
max_len = 0
seen = {0: -1}

for i in range(n):
    prefix += arr[i]

    if prefix - k in seen:
        max_len = max(max_len, i - seen[prefix - k])

    if prefix not in seen:
        seen[prefix] = i

print(max_len if max_len > 0 else -1)