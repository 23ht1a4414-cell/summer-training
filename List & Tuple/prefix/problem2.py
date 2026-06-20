
#find the multiple range queries 1-4  2-5 0-3, all queries in a single program
arr = [2,4,1,7,3]
queries = [(1,4),(2,4),(0,3)]
prefix = [0]*len(arr)
prefix[0] = arr[0]
for i in range(1, len(arr)):
    prefix[i] = prefix[i-1] + arr[i]
for l,r in queries:
    if l == 0:
        sum = prefix[r]
    else:        
        sum = prefix[r] - prefix[l-1]
    print(sum)