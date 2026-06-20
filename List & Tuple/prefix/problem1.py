#find sum from 1 to 3
arr = [2,4,1,7,3]
l = 1
r = 3
prefix = [0]*len(arr)
prefix[0] = arr[0]
for i in range(1, len(arr)):
    prefix[i] = prefix[i-1] + arr[i]
print(prefix)
if l == 0:
        sum = arr[i]
else:        
    sum = prefix[r] - prefix[l-1]
print(sum)