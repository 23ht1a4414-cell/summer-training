











'''def function _name (parameters):
"""Doc strings"""
statements
return value

def-->keyword


'''
#create a function
def hello():
    print("Hello world")
#call the function
hello()
#parameters: variable passed during function call
def add(a,b):
    print(a+b)
add(2,3)
'''
types of arguments:
1.positional arguments:
arguments passed in order
'''
#Example:
def multiply(a,b):
  print(a*b)
  return a*b
multiply(2,3)


#task:create a fun to calculate
#simple interest using positional args

def simple_interest(p,r,t):
    si = (p*r*t)/100
    print(si)
simple_interest(100,5,2)
2#keyword arguments: 
def sub(a,b):
    return a -b
sub(b = 5,a=10)
#task :call the simple interest fun
#using keyword arguments

simple_interest(p=100,r=5,t=2)
#3. default arguments:
def student(name,branch = "CSE"):
    print(f"Hello {name} from {branch}")

student("loki")
#task:create a fun to cal
#square by default parameters
def square(num=2):
    print(num**2)
square()

#4variable length arguments
def total (*args):
    print(args)
    print(sum(args))
    print(max(args))
#call the fun
total(10,20,30,40)
#task:create a fun to find sum of any number of values
def total(*values):
    print(sum(values))
total (10,20,30,40,50,60,70,)
'''
#kwargs -->keyword arguments
def student_details(**kwargs):
print(kwargs)
'''
def student_details(**kwargs):
    print(kwargs)
student_details(name = "lokesh",branch =" CSD",rollno = "14")
#create a fun to print employee details
#using kwargs

def employee_details(**kwargs):
    print(kwargs)
employee_details(name = "lokesh",id = "14",department = "IT")
#create a fun to print employee details
#using kwargs
#task:write args and kwargs together
def details(*args,**kwargs):
    print(args,kwargs)
   
details(10,20,30,name = "lokesh",id = "14",department = "TCS")
'''
return statement:send the value
back to the caller

def add(a,b)
return a+b


result = add(10,20)
print(result)


print                 |            return
display the O/P                 sends the value 
can't reuse                    can reuse

multiple return values:
def calculate (a,b):
return a+b,a-b,a/b

format = tuple

s,sub,div = calculate(20,30)
'''
def calculate (a,b):
    return a+b,a-b,a/b


s,sub,div = calculate(20,30)
print(s,sub,div)
#task:create a fun that returns
#1.min,2.max,3.avg of the numbers
def stats(*args):
    minimum = min(args)
    maximum = max(args)
    average = sum(args)/len(args)
    return minimum,maximum,average

min, max, avg = stats(10, 20, 30, 40, 50)
print(min, max, avg)
'''
#function doc strings

doc string describes:
1.what function does
2.parameters
3.return value
def add(a,b)
"""this function adds 2 numbers & returns result"""
return a+b
'''
def add(a,b):
    """this function adds 2 numbers & returns result"""
    return a+b
print(add.__doc__)
print(help(add))
#task:write a docstring for the simple interest program

def simple_interest(p,r,t):
    """this function calculates simple interest using the formula SI = (P*R*T)/100
    where P is the principal amount, R is the rate of interest, and T is the time in years.
    It returns the calculated simple interest."""
    si = (p*r*t)/100
    return si
print(simple_interest.__doc__)
print(help(simple_interest))

'''
variable scopes:
1.local scope:
variables declared inside the function
def test ():
    x = 100
    print(x)
    
2.Global scope:
def show ():
    x = 200
    print(x)
    show()'''
def test():
    x = 100
    print(x)
test()
def show ():
    x = 200
    print(x)
show() 
#accessing the local scope outside the fun
x =0
def update():
    x = x + 5

print(x)
#task: try without using global and tell me error
'''
task:
create a function banlk-trasaction
which accepts
1.accounts holder(string)
2.balance
3.transaction_type(deposit/withdraw)
4.amount
by using :
1.def arguments
return statements
global balance
'''
balance = 100000
def bank_transaction(account_holder,transaction_type,amount):
    global balance
    if transaction_type == "deposit":
        balance += amount
        print(f"{account_holder} deposited {amount}. New balance: {balance}")
    elif transaction_type == "withdraw":
        if amount > balance:
            print(f"{account_holder} has insufficient funds for withdrawal.")
        else:
            balance -= amount
            print(f"{account_holder} withdrew {amount}. New balance: {balance}")
    else:
        print("Invalid transaction type. Please use 'deposit' or 'withdraw'.")
bank_transaction("Anaas", "deposit", 500)
bank_transaction("akhil", "withdraw", 200)
bank_transaction("lokesh", "withdraw", 1500)
'''
Lambda function: is a small &anonamous function
#function without name
# defined using lambda
can passs any number of atguments
can have only one expression
returns the value automatically(no return key)
normal function:
def add(a,b)
 retutn a+b
#write using lambda
#add = lambda a,b:a+b
#calling the function
add(10,20)

'''
#task:write a normal fun to square of num convert the normal fun to lambda
def square(n):
    return n**2

square_lambda = lambda n: n**2
print(square_lambda(5))

'''
arr = list(map(int,input().split()))
#map():applies the function each element of iterable
map (function,iterable)

Example:
def square(x):
   return x*x
   
nums = [1,2,3,4]
result = list(map(square,nums))
print(result) 
'''
def square(x):
   return x*x
   
nums = [1,2,3,4]
result = list(map(square,nums))
print(result)
def square(x):
   return x*x
   
nums = [1,2,3,4]
result = list(map(lambda x:x*x,nums))
print(result)
#task:given a list of numbers
#

'''
what is filter?
selects the elements based upon the condition

syntax:
filter(function,iterable)

Example:
def is_even(x):
   return x%2==0

list = [1,2,3,4,5,]
result = filter(is _even,list)
print(result)
'''
#task:given with list with frnds names
#filter the names letter starting with A
friends = ["Arjun", "Lokesh", "Anas", "Ram", "Akhil", "Sri"]

a_names = list(filter(lambda v: v.startswith("A"), friends))

print(a_names)

'''
what is reduce()?
repeatedly applies function
reduces the iterables to single value

syntax:
reduce(function,iterables)
'''
#functools ---> module
from functools import reduce

nums = [1,2,3,4,5]
result = reduce(lambda a,b:a+b,nums)
print(result)