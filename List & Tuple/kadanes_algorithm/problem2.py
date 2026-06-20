'''#max product subarray
I/P : [2,3,-2,4]
O/P : 6'''


arr = [2,3,-2,4]
current_sum = arr[0]
max_sum = arr[0]
starting_index = 0
ending_index = 0
for i in range(1, len(arr)):
    if current_sum * arr[i] > arr[i]:
        current_sum *= arr[i]
    else:
        current_sum = arr[i]
        starting_index = i
    if current_sum > max_sum:
        max_sum = current_sum
        ending_index = i
print(max_sum)
print(starting_index)
print(ending_index)
print(arr[starting_index:ending_index+1])