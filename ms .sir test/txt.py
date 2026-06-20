'''

given an integer array Arr of size N,
find the count of elements whose value is
greater than all of its prior elements.
the 1st element is always considered in the count
I/P:Arr = {7,4,8,2,9}
O/P:3
'''
ar =(7,4,8,2,9)
count = 0
a = ar[0]
for i in range(len(ar)):
        if a <= ar[i]:
         count += 1
        a = ar[i]
print(count)