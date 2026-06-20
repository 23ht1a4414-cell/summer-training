'''Decorators:
adds the extra functionality
without changing the original function
Gift wrapper:
extra layer , beauty
Decorator = wrapper around the function
#why Decorator are needed?
logging:
authentication,
timing,
validation

if no Decorator:
1.repeated code
2.messy programs
'''
#in python -- funtion are #treated as 
def greet():
    print("hello lokesh")
x = greet
x()
#nested function
def outer():
    def inner():
        print("inner side")
    return inner()
x = outer
x()
#simple Decorator:
def decorator_function(original_function):
    def wrapper():
        print("Before function call") 
        original_function()
        print("after function call") 
    return wrapper
#original function:
def greet():
    print("hello lokesh")

#simple manually
decorated = decorator_function(greet)
decorated()
'''
greet()
|
decorated_function()
|
wrapper created()
|
extra functionality is added

special symbol : @
'''
# ex-2
def smart_divide(func):
    def wrapper():
        print("checking before div")
        func()
        print("division is completed")
    return wrapper
@smart_divide
def divide():
    print(10/2)
divide()
#ex-3
def decorator_function(original_function):
    def wrapper(name):
        print("Before function call") 
        original_function(name)
        print("after function call") 
    return wrapper
@decorator_function
def greet(name):
    print("hello",name)

greet("loki")
#ex-4
#timer decorator
import time
def timer(func):
    def wrapper():
        start = time. time()
        func()
        end = time. time()
        print("Execution time", end-start)
    return wrapper
@timer
def test():
    for i in range(10000):
     pass
test()
#ex
def login_required(func):
    def wrapper():
        print("checking the user login")
        func()
    return wrapper
@login_required
def dashboard():
    print("welcome to dashboard")
dashboard()