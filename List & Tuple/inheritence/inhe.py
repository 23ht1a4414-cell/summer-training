'''
What is inheritence?
a mechanism where one class acquire the properties and methods of another class
            or
one class reuses the features of another class            

Simple understanding:
a class can use variables,use methods of parent class

Example:
vehicles:
car,bike,bus

all vehicle have 
start(),stop()
no need to repeated code

write code once
        |
use number of times

advantages or why?
1.code reusability
2.Reducing the code duplication
3.Better organization
4.Easy Maintenance

Terms:
parent:Base or Super class
Child:
sub class/derived

Parent
|
child
'''
#syntax:
class parent:
    pass
class Child:
    pass

#Example:
class Animal:
    def eat(self):
        print("Animal is eating")
#child class        
class Dog(Animal):
    pass        
#have to create object for child class
d1 = Dog()
d1.eat()
'''
Dog class does not contains eat()
                |
 python searches in animal class
                |
 method is found and execute
 '''
#no inheritence
class dog:
    def eat(self):
        print("eating")
class cat:
    def eat(self):
        print("eating")
#with inheritence
class animal:
    def eat(self):
        print("eating")
class dog(Animal):
    pass
class cat(Animal):
    pass
c1=cat()
c1.eat()

#accessing the parent variable
class Animal:
    def __init__(self):
        self.name = "Loki"
class Student(Animal):
    pass        

s1 = Student()
print(s1.name)

'''
''
Types of inheritence in python
1.single inheritence
2.Multiple Inheritence
3.Multi level inheritence
4.Hierarichal inheritence
5.Hybrid inheritence
''
#1.Single Inheritence
one child inherites one parent class
                parent
                  |
                child
'''


#Example:
class Animal:
    def eat(self):
        print("eating")
class Dog(Animal):
    def bark(self):
        print("Barking")

d1 = Dog()
d1.eat()
d1.bark()

'''
#2.Multiple Inheritence:
one child class inherits multiple parent class
            parent1             parent2
                  \              /
                         Child

'''
class Father:
    def money(self):
        print("Fathers money")
class Mother:
    def gold(self):
        print("Mother gold")
class child (Father,Mother):
    pass
c1=child()
c1.gold()
c1.money()
'''
''
3.Multi level inheritence:
Inheritence chain of multiple levels
                Grand parent
                    |
                 parent
                    |
                  Child '''  
 
class Grandparent:
    def house(self):
        print("Gandparents Home")
class Parent(Grandparent):
    def car(self):
        print("Parents car")
class Child(Parent):
    def bike(self):
        print("Childs bike")
c1 = Child()
c1.house()
c1.car()
c1.bike()    
'''
#4.Hierarichal inheritence
muiliple child class inherit from one parents

         parent
        /      \
    child1  child2

'''
class animal:
    def eat(self):
        print("eating")
class dog(animal):
    def bark(self):
        print("barking")
class cat(animal):
    def meow(self):
        print("meow")
c1=cat()
c1.eat()
'''
'''
#5.Hybrid inheritence

#two or more inheritence types:
#1.hirearichal and multiple
#   A
 #/    \
 #B    C
 #\    /  
  #  D'''


class A:
    def show_a(self):
        print("class A")
class B(A):
    def show_b(self):
        print("class B")
class C(A):
    def show_c(self):
        print("class C")
class D(B,C):
    def show_d(self):
        print("class D")
d1 =D()
d1.show_a()
d1.show_b()
d1.show_c()
d1.show_d()

class animal:
    pass
class dog(animal):
    pass
c1 = dog()
print(isinstance(c1,dog))
print(isinstance(dog,animal))
class parent():
    def __init__(self):
        print("constructer called")
class child(parent):
    pass
c1=child()
'''
problem:1
create a parent class animal with method sound() that should print animal makes sound
'''
class animal:
    def sound(self):
        print("animal makes sound")
class dog(animal):
    pass
c1=dog()
c1.sound()
'''
problem:2
create a parent class college
class variables --->college _name
create a child class student
instance variables -->student_name
display:
1.college _name
2.student_name
'''
class college:
    college_name = "bokada"
class student(college):
    def __init__(self,student_name):
        self.student_name = student_name

s1 = student("Anas")
print(s1.college_name)
print(s1.student_name)
'''create:
vehicle class with method start()
car class inheriting vehicle
sportscar class inheriting the car
add method:
speed()
inside the sports car1:
call:
start()
'''

class vehicle:
    def start(self):
        print("vehicle is starting")

class car(vehicle):
    def __init__(self):
        super().__init__()

class sports_car(car):
    def speed(self):
        print("sports car is speeding")
s1 = sports_car()
s1.start()
s1.speed()
'''
employee skill system
create:
class programmeer with method coding()
class designer with method designing()
create a child class employee inheriting
both classes
all both methods using employeeobjects

'''
class programmer:
    def coding(self):
        print(" coding")

class designer:
    def designing(self):
        print("designing")

class employee(programmer, designer):
    pass

e1 = employee()
e1.coding()
e1.designing() 
'''
Employee Bonus Mgmt
A company wants to calc
yearly bonuses for 
different types of employees 

create a base class Employee:
with:
name , salary 
create method:
calculate bonus()

then create two child classes 
developer
Bonus = 20% of salary 
manager 
Bonus = 35% of salary 
write a program to:
1.Take employee details as input
2.create objects based on employee type
3.Display:
employee name 
role
Bonus amount 

input format:
role,name,salary

output format:
Name:<name>
Role:<role>
Bonus:<bonus>

Sample:
3
Developer Rahu1 50000
Manager   Sneha 80000
Developer Arjun 60000

output:
Name:Rahul
Role:Developer
Bonus:10000.00
'''

'''''
#Online course Access System
An online learning platform provides 
different levels of course access
create a parent class Course: with
-> Student_name 
create a method:
access_level():
Then create two child classes 
->FreeCourse
Access Level = "Limited Access"
->Premium Course 
Acess Level = "Full ACcess"
write a program:
1.Accept student details 
2.Create objects using inheritance 
3.Print Student access information

input:course_type,student_name

sample:
4
Free Amit
Premium Neha
Free Rohan
Premium Rakesh

output:
Student:Amit
Course_type:Free
Access:Limited Access
    
'''
class Course:
    def __init__(self, student_name):
        self.student_name = student_name

    def access_level(self):
        pass


class FreeCourse(Course):
    def access_level(self):
        return "Limited Access"


class PremiumCourse(Course):
    def access_level(self):
        return "Full Access"


n = int(input())

for i in range(n):
    course_type, student_name = input().split()

    if course_type == "Free":
        student = FreeCourse(student_name)
    elif course_type == "Premium":
        student = PremiumCourse(student_name)

    print("Student:", student_name)
    print("Course_type:", course_type)
    print("Access:", student.access_level())