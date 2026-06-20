'''
Prefix Sum: one of the most inportant technique used to solve the subarray problems
1.Fast range sum queries
2.optimization
3.sliding windows alternative
4.subarray problems
5.competitive programming

It reduces the repeated calculations and imports the tie complexity

What is prefix sum?
stores the cumulative sum of the elements
from the beginning of the array to every index


arr = [a0,a1,a2,a3.....]

prefix[i] = arr[0]+arr[1]+arr[2]....+arr[i]

problem:
arr = [2,4,1,7,3]
       0 1 2 3 4 

find the sum from index 1 to 3

'''
arr = [2,4,1,7,3]
l = 1
r = 3
total = 0
for i in range(l,r+1):
    total +=arr[i]
print(total) 
'''
Prefix sum -->
arr = [2,4,1,7,3]
       0 1 2 3 4

calculate the prefix:
index   arr[i]  prefix[i]
0          2        4
1          4        2+4 = 6
2          1        6+1 = 7
3          7        7+7 = 14
4          3        14+3 = 17

prefix[i] = [2,6,7,14,17]

prefix[0] = 2   sum from 0 to 0
prefix[1] = 6  sum from 0 to 1
prefix[2] = 7   sum from 0 to 2
prefix[3] = 14   sum from 0 to 3
prefix[4] = 17   sum from 0 to 4

prefix sum formula:
sum = prefix[R]-prefix[L-1]

find sum from 1 to 3

R = 3
L = 1

sum = prefix[3] - prefix[0]
sum = 14 - 2 = 12

'''



'''
 find the Equilibrium index using prefix sum
 left sum = right sum

'''
arr = [1,3,5,2,2]
prefix = [0]*len(arr)
prefix[0] = arr[0]
for i in range(1, len(arr)):
    prefix[i] = prefix[i-1] + arr[i]
total_sum = prefix[-1]
a = 0
for i in range(len(arr)):
    left_sum = prefix[i-1] 
    right_sum = total_sum - prefix[i]
    if left_sum == right_sum:
        a = i
        break
print(a)

