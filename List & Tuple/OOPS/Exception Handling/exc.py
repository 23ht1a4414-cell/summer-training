'''


Error:An error is a problem in the program causing abnormal termination

1.Syntax Error
2.Run time errors --Exceptions
    ---> Occurs while executing the program

    Example:
    a = 10
    b = 0
    c =a/b --> ZeroDivisionError

    3.Logical Errors:
    Program runs but gives wrong output
    Example:

    print(2*(3+5))

what is exception handling:
Exception handling is a mechanism to handle 
run time errors gracefully without stopping the program

without exception:
1.Program crashes
2.Poor User experience
3.Data loss possible

with exception:
1.Program will execute manually
2.Proper error message
3.Safer application

#basic Exception:
syntax:

keywords:try,catch,finally,raise

try:
   risky code
except:
   handling code


'''

#lets write our first program
#try:
 #   num = int(input("Enter a number:"))
  #  print(10/num)
#except:
 #   print("Some error occured")

#Risky code will be inside try
#if exception occurs ->except executes

#above is not a good practice
#Hides actual problem
#difficult to debug
try:
    num = int(input("Enter a number:"))
    print(10/num)
except ZeroDivisionError:
    print("Cannot divide with 0")

except ValueError:
    print("Input should not be a string")


'''
Common python exceptions:
1.ZeroDivisionError ---> Divide with 0
2.ValueError: ---> Invalid input
3.TypeError: ---> Wrong datatype
4.IndexError ---> Invalid Index
5.KeyError ---> Invalid dictionary key
6.FileNotFoundEroor ---> File Missing
7.Attribute Error ---> Invalid Attribute
8.NameError ---> Variable is not defined

'''
#Example:
try:
    list = [10,20,30]
    index = int(input("Enter the index:"))
    print(list[index])

except IndexError:
    print("Index out of range:")

except ValueError:
    print("Please enter integer:")

#Else:if no exception occurs 
'''
try:
   code
except:
   handling
else:
   success block

'''
try:
    list = [10,20,30]
    index = int(input("Enter the index:"))
    print(list[index])

except IndexError:
    print("Index out of range")

except ValueError:
    print("Please enter integer")

else:
     print("No Exception Occured")

#another Example:
try:
    num = int(input("Enter the number:"))
    result = 100/num
except ZeroDivisionError:
    print("Zero")
else:
    print(result)

#finally
'''
finally block executes always
used for:
1.closing files
2.closing database connections
3.cleanup activities

try:
   code
except:
   handling
finally:
   cleaning code
'''
#try:
 #   File = open("data.txt")

#except FileNotFoundError:
#   print("File not found")

#finally:
#    print("Execution completed")
try:
    print("transactiion is processing")
except:
    print("Transaction failed")
finally:
    print("Thanks for using ATM")

try:
    a = 10/0
except ZeroDivisionError as e:
    print("Error:",e)

#Nested try blocks
try:
    print("outer try")
    try:
        num = int(input("Enter number"))
        print(10/num)
    except ZeroDivisionError as e:
        print("Error:",e)
except:
    print("Outer Exception")

#generate exceptions

age = int(input("Enter the age:"))
if age<18:
    raise ValueError("Age should be 18 or greater:")
print("Eligible")
#why custom execeptions;
class MyExeception(Exception):
    pass
#Bank Application
class InsufficientBalance(Exception):
    pass
balance = 5000
withdraw = int(input("enter the amount"))
if withdraw > balance:
    raise InsufficientBalance("Not enough balance")
print("withdraw successful")


#task:write a custom exeception
class food(Exception):
    pass
food_item = input("Enter the food item:")
if food_item.lower() not in ["pizza","burger","pasta"]:
    raise food("Food item not available")
print("Order placed successfully")
#student results
class student(Exception):
    def __init__(self,marks):
        self.marks = marks
    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 80:
            return "B"
        elif self.marks >= 70:
            return "C"
print("Enter the marks:")
marks = int(input())
try:
    s = student(marks)
    grade = s.calculate_grade()
    print("Grade:",grade)
except Exception as e:
    print("Error:",e)
s1 = student([])
s1.calculate_grade()
#login system
class Loginsystem(Exception):
    pass
username = input("Enter username:")
password = input("Enter password:")
if username != "admin" or password != "admin123":
    raise Loginsystem("Invalid credentials")
print("Login successful")
