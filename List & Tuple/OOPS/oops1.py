'''
cnstructor : __init__()
special method
automatically called when object is created

used:initilizing the object data

'''
class student:
    def __init__(self):
        print("constructor is called")
s1 = student()
s1.__init__

'''
student()
|
object created
|
__init__automatically

if no constructor
manually assign the value


if yes
automaric initialization

'''
class student:
    pass
s1 = student()
s1.name ="lucky"
s1.branch ="DS"
print(s1.name)
print(s1.branch)

#example
class student:
    def __init__(self):
        self.name ="loki"
        self.age ="22"
obj1 = student()
print(obj1.name)
print(obj1.age)
'''
self-->current object(obj1)
self-->obj1

#constructor with parameter

'''
class student:
    #constructor
    def __init__(self,name,age):
        self.name = name
        self.age = age
obj2 = student("sri",28)
print(obj2.name)
print(obj2.age)
'''
self --->obj2
name:"hsekol"
age:21

obj2
name="hsekol"
age=21
 
step by step:
1.object memory allocation
2.__init__is called automatically
3.self points tothe object
4.variables initialized
5.object returned

'''
'''
#default constuctor:

class Test:
def__init__(self):
print("default constuctor")
t = Test()
parametrized constuctor
class Test:
 def __init__(self.x):
 
self.x =100
t -test()                 |normal method
constructor:              |manually call it
automatically called      |any name
name fixed:__init__       |used for operations
used for initialization   |executes when called

'''
class student:
    def __init__(self):
        print("contructor")
    def display (self):
        print("normal method")
c1 = student()
c1.display()
'''
Instance variables:
variables that belong to an object
seperate copy created for every object

They store:
     object specific data 

Student | Name |Marks
s1       lokesh  10
s2       loki    30
Each obj stores its own data
'''

class student:
    def __init__(self,name ,marks):
        self.name = name
        self.marks = marks
s1 = student("lokesh",98)
s2 = student("python",97)
print(s1.marks)
print(s2.marks)
'''
s1 obj
-------
name ="lokesh"
marks =98

s2 obj
-------
name ="python"
marks =97
object do not share instance variables

'''
#Instance methods
class Student:
    def __init__(self,name ,marks):
        self.name = name
        self.marks = marks
    def display(self):
        print(self.name)
        print(self.marks)
s1 = Student("loki",98)
s1 .display()
'''
class variables:
shared among all the object
'''
class student:
    #class variables
    college_name = "cit"
    def __init__(self,branch):
        #instance variable
        self.Branch = branch
s1 = student("ds")
print(s1.college_name)
'''
self:refers tom current object
        (or)
reference variable poining to current object

'''
class student:
    def display(self):
        print("hey")
s1= student()
s1.display()
'''
s1.display()
|
student.display(s1)
|
self-s1(self points to s1)
'''
class student:
    def show(self):
        print("self")
s1 =student()
s2 =student()
print(s1)
print(s2)
s2.show()
'''
student class
-------------
clg = cit #stored in class 
--------------------------
       |           |
       s1         s2
       
       
    class employee:
        company = "google"
        def display(self):
            print(self.company)
    e =employee()
    two ways access:
    print(e.company)
    #no object use
    print(employee.company)
    '''
'''
#class methods:
work with class variables
operate on class level data

@classmethod - decorator

  '''
#Basic example for class method
class student:
    college = "loki"
    @classmethod
    def show_college(cls):
        print(cls.college)
student.show_college()
'''
@classmethod:
decorator which tells python:
this method belongs to class not object
self -->current object
cls -->current class
'''
#task:
#create a class named as employee
# create one class var
# use @classmethod to apply
# on method company_name
# print the company name
# using multiple objects
class employee:
    company = "infos"
    @classmethod
    def company_name(cls):
        print(cls.company)
e1 = employee()
e2 = employee()
e1.company_name()
e2.company_name()
'''
diff b/w instance method and class method

instance method            |   class method
works on the objects data  |  works on class data
uses self                     cls--current class
need object                   directly using class
access the instance var  access class varbles
'''
class stu:
    clg ="lokesh"
    #instance method
    def instance(self):
        print("instance method")
    @classmethod
    def class_method(cls):
        print("class method")
l1 =stu()
l1.instance()
'''
static method:
doesn't uses:object,class
they are:
utility /helper methods
not uses:
self,cls

example:
add()
multiply()
@staticmethod-->decorator
'''
#static method example
class calculator:
    @staticmethod #helper method
    def add(a,b):
        return a+b
print(calculator.add(10,20))

class message:
    @staticmethod
    def greet():
        print("hello lokesh")
print(message.greet())

# task :create a class named as student
#create constuctor
#class varible
#instance varible
#instance method
#class method
#static method
class student:
    college = "lokesh"
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print(self.name)
        print(self.age)
    @classmethod
    def show_college(cls):
        print(cls.college)
    @staticmethod
    def greet():
        print("lokesh")
l1 = student("loki",22)
l1.display()
student.show_college()
student.greet()




    




 





