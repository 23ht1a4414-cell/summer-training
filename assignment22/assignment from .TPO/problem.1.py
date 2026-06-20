'''A company tracks employee activities using the format: 
Employee Name: TaskCompleted 
The activities are stored in a list. 
You need to generate a productivity report. 
Rules 
1. Count the number of tasks completed by each employee.  
2. Employee names are case-insensitive.  
3. Print employees in descending order of tasks completed.  
4. If two employees have the same task count, print them in alphabetical order.  
Input 
7 
John:Login 
Alice:Testing 
john:Development 
Alice:Documentation 
Bob:Testing 
John:CodeReview 
alice:BugFix 
Output 
john 3 
alice 3 
bob 1
'''
n = int(input())

tasks = {}

for _ in range(n):
    emp, task = input().split(":")
    emp = emp.strip().lower()

    if emp in tasks:
        tasks[emp] += 1
    else:
        tasks[emp] = 1

result = list(tasks.items())

for i in range(len(result)):
    for j in range(i + 1, len(result)):
        if result[i][1] < result[j][1]:
            result[i], result[j] = result[j], result[i]
        elif result[i][1] == result[j][1]:
            if result[i][0] > result[j][0]:
                result[i], result[j] = result[j], result[i]

for emp, count in result:
    print(emp, count)