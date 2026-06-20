'''
Module:
a module is simply a python file containing code

why?
1.Large file
2.hard to maintain
3.difficuilt to reuse

modules:
reusability
organization
Readibility
collabration
'''
import calculator
print(calculator.add(1,3))
print(calculator.sub(3,5))

#create a module named as greeting
import greeting
greeting.greetings("lokesh")
greeting.greet("loki")


import math
print(math.sqrt(44))
print(math.factorial(5))



#from import
from math import sqrt,pow
sqrt(3)
pow(2,2)

import math
import random
  #or
import math,random

#all the attributes from math
#from math import*
#from Looping.new import hello
#hello()

#collection of modules is called package
import datetime as dt
print(dt.datetime.now())

'''
Module          meaning
1.math        mathmatics
2.random       random variables
3.datetime     date & time
4.os           operation
5.sys          system

'''

#help("modules")
'''
#package:
the folder containing  multiple modules

school/  ---> package
   student.py
   teacher.py
   management.py

   
main.py ---> from school import student

__init__.py
purpose:
special file used to identity package
1.marks directory as package
2.Runs intialization code
3.controls the import

'''
#import school.student import show_student
#how_student()


# bulit in methods
import math

#round upward
print(math.ceil(5.2))

#floor()--->
print(math.floor(5.2))

#constants
print(math.pi)
print(math.e)

#task:Area of a circle
radius = float(input("Enter radius: "))

area = 3.14 * radius * radius

print("Area of circle =", area)

#random bulit 

import random

#randint()
print(random.randint(1,100))

#choice
fruits = ["apple","banana","pine"]
print(random.choice(fruits))

#shuffle()
cards = [1,2,3,4]
random.shuffle(cards)
print(cards)

#task:bulid the dice simulator
import math

print(random.randint(1, 6))
#date
import datetime
print(datetime.date.today())

#custam date
d = datetime.date(2026,6,18)
print(d)

#bulid the age calcuator
import datetime
birth_year =2005
current_year = datetime.date.today().year
print(current_year-birth_year)

import os

print(os.getcwd())

#mkdir  --make directory
#print(os.mkdir("pythonclass"))

#change the name
#os.rename("pythonclass","2027 Batch")

#listdir()
#print(os.listdir())


#remove directory
#os.rmdir("2027 Batch")

#Task:Display all the files in dir
import os
files = os.listdir()
for files in files:
    print(files)

#Modules - sys
#provides the info about python interpreter

import sys
print(sys.version)


print(sys.exit())
print(sys.path())