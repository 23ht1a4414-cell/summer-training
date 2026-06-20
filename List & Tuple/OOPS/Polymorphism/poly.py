'''
what is polymorphism?
poly-->many
morphism-->forms
same method/operators will behave differently

Example:

print(5+3)#8
print("hello"+"world") #helloworld

          same operator
              | 
         but diff behaviours
         
Types of polyphism
 1.compile time
 2.run time polyphism'''

#1.compile time --method overloading
'''no method overloading in python
#though its not there,in order to achieve in python we use *args

method overloading:
is same method names + different parameters
is not possible in python
to overcome or to handle overloading in python , python uses *args(variable length arguments)

method overloading:
is same method names +same parameters
is possible in python         


#java --> add(int, int)
#  ---> add (int,int,int)


python approach:
class calculator:
    def add(self,a,b,c = 0):
        print(a + b + c)
        
c1 = calculator()
c1.add(10,20)
c1.add(10,20,30)

'''
#2.Run time polyphism:
'''
-->using method overriding

'''
class bird:
    def fly(self):
        print("bird's flying")
class eagle(bird):
    def fly(self):
        print("eagle's flying")
c = eagle()
c.fly()

#Duck typing in python
'''python focuses on behaviour not object type

'''
class duck:
    def sound(self):
        print("quack")
class dog:
    def sound(self):
        print("bark")
def make_sound(obj):
    obj.sound()
d1 = duck()
d2 = dog()

make_sound(d1)
make_sound(d2)