'''
company wants to generate employee salary reports
1.Accept employee details
2.store them in employee.txt
3.calculate total salary expenditure
total = 0 + salary
4.display employee report

'''
total = 0
try:
    file = open("employee.txt", "w")

    n = int(input("Enter number of employees: "))

    for i in range(n):
        name = input("Enter employee name: ")
        salary = float(input("Enter salary: "))
        total += salary

        file.write(name + " " + str(salary) + "\n")

    file.close()

    print("\nEmployee Salary Report:")
    print("Total Salary Expenditure:", total)

    file = open("employee.txt", "r")

    for line in file:
        print(line.strip())

    file.close()

except FileNotFoundError:
    print("File not found!")

except ValueError:
    print("Invalid input!")

except Exception as e:
    print("Error:", e)

