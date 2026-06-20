'''OOPS:object oriented programming (paradigram)
programs are organized using objects
objects contain
1.data(variables)
2.behaviour(function/methods)


car -->object
student -->object


Each object here:
will have properties and actions
        |           |
    variables   methods
 Earlier the programming was written wasa without loops

 1.difficuilt to manage the large level projects
 2.code duplication
 3.less security
 4.difficilt maimtenance

 ooops solve the above problems
 1.classes
 2.objects
 3.encapsulation
 4.Inhritance
 5.abstraction
 6.polymorphism

'''
#procedural programming
name = "Ramya"
marks = 100
def display():
    print(name,marks)

display()
#oop approach
class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def display(self):
        print( self.name,self.marks)
s1 = student("ramya",12)
s1.display()
'''
advantages:
1.code reuasability
2.Better organization - modular and structure
3.security -> encapsulation
4.Easy maintenance: update , debug
5.real world modelling
6.scalability : large application

'''
'''
class:Blueprint of an object
collection of var,mathods ??

Blueprint:
can be used to build many houses

'''
class ClassName:
    pass
'''
class:keyword creates class
classname:identifiers
pass:empty block

'''
#object: instance of a class
          #(or)
#Actual Memory representation of class
class student:
    pass
#create an object
obj = student()
print(obj)
'''
object: instance name (object)
student --->class name

'''
class car:
    brand = "audi"
    def start(self):
        print("car started")
#create the objects
#both objects has different memory locations
c1 = car()
c2 = car()
(c1.start())
(c2.start())
c1.brand
#class --.>obj searches


#task:
'''
# create a class named as employee
#create 2 variables company name and id
#create 2 methods to access name and company_name
# create 2 objects and access variables and name
'''
class employee:
    company_name ="infocs"
    id = "4414"
    name = "loki"
    def name(self):
        print("loki")
    def company_name(self):
        print("infocs")
e1 = employee()
e2 = employee()
e1.name()
e2.company_name()
print(e1.id)
